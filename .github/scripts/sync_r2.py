#!/usr/bin/env python3
"""Upload this checkout to R2. Skip objects that already have the same size."""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.cloudflare.com/client/v4"
ACCOUNT = os.environ["R2_ACCOUNT_ID"]
BUCKET = os.environ["R2_ASSETS_BUCKET"]
TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
PUBLIC = os.environ.get("R2_PUBLIC_BASE_URL", "").rstrip("/")
ROOT = Path(os.environ.get("SYNC_ROOT", ".")).resolve()
CACHE_CONTROL = "public, max-age=604800"
USER_AGENT = "ultra-hercules-assets-sync"
SKIP_DIRS = {".git", ".github"}
SKIP_NAMES = {".DS_Store"}
CONTENT_TYPES = {
    ".mp3": "audio/mpeg",
    ".m4a": "audio/mp4",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".glb": "model/gltf-binary",
}


def request(method, url, data=None, headers=None, timeout=300):
    for attempt in range(6):
        hdrs = {"Authorization": f"Bearer {TOKEN}"}
        if headers:
            hdrs.update(headers)
        req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.status, response.read()
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", "replace")
            if error.code in (429, 500, 502, 503, 504) and attempt < 5:
                retry_after = error.headers.get("Retry-After", "")
                wait = int(retry_after) if retry_after.isdigit() else min(60, 2**attempt)
                print(f"retry {error.code} in {wait}s", flush=True)
                time.sleep(wait)
                continue
            raise SystemExit(f"{method} failed {error.code}: {detail[:500]}") from error
    raise SystemExit(f"{method} failed after retries")


def list_remote():
    sizes = {}
    start_after = None
    while True:
        query = "per_page=1000"
        if start_after:
            query += "&start_after=" + urllib.parse.quote(start_after, safe="")
        _, body = request(
            "GET",
            f"{API}/accounts/{ACCOUNT}/r2/buckets/{BUCKET}/objects?{query}",
        )
        payload = json.loads(body)
        objects = payload.get("result") or []
        if isinstance(objects, dict):
            objects = objects.get("objects") or []
        if not objects:
            break
        for obj in objects:
            sizes[obj["key"]] = int(obj["size"])
        if len(objects) < 1000:
            break
        start_after = objects[-1]["key"]
    return sizes


def encode_key(key):
    return "/".join(urllib.parse.quote(part, safe="") for part in key.split("/"))


def content_type(path):
    return CONTENT_TYPES.get(path.suffix.lower(), "application/octet-stream")


def local_files():
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        for name in filenames:
            if name in SKIP_NAMES:
                continue
            full = Path(dirpath) / name
            if not full.is_file():
                continue
            found.append((full.relative_to(ROOT).as_posix(), full))
    return found


def upload(key, path):
    size = path.stat().st_size
    url = (
        f"{API}/accounts/{ACCOUNT}/r2/buckets/{BUCKET}/objects/{encode_key(key)}"
    )
    data = path.read_bytes()
    request(
        "PUT",
        url,
        data=data,
        headers={
            "Content-Type": content_type(path),
            "Content-Length": str(size),
            "Cache-Control": CACHE_CONTROL,
        },
        timeout=max(180, size // (256 * 1024)),
    )


def sample_keys(files):
    present = {key for key, _ in files}
    chosen = [
        key
        for key in (
            "audio/ultra_hercules_010001.mp3",
            "audio/ultra_hercules_010025.mp3",
            "audio/ultra_hercules_010303.mp3",
        )
        if key in present
    ]
    nested = sorted(
        key for key in present if key.startswith("audio/04/") and key.endswith(".mp3")
    )
    if nested:
        chosen.append(nested[0])
    images = sorted(
        key
        for key in present
        if key.startswith("img/")
        and key.rsplit(".", 1)[-1].lower() in {"jpg", "jpeg", "png", "webp", "gif"}
    )
    if images:
        chosen.append(images[0])
    return chosen


def range_check(url):
    for attempt in range(4):
        req = urllib.request.Request(
            url,
            headers={"Range": "bytes=0-1023", "User-Agent": USER_AGENT},
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                return (
                    response.status,
                    response.headers.get("Accept-Ranges", ""),
                    response.headers.get("Content-Range", ""),
                )
        except urllib.error.HTTPError as error:
            if error.code in (403, 429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2**attempt)
                continue
            return (
                error.code,
                error.headers.get("Accept-Ranges", ""),
                error.headers.get("Content-Range", ""),
            )
    return 0, "", ""


def verify(keys):
    if not PUBLIC:
        raise SystemExit("R2_PUBLIC_BASE_URL is empty")
    failed = False
    for key in keys:
        status, accept, content_range = range_check(f"{PUBLIC}/{encode_key(key)}")
        ok = status == 206 and content_range.lower().startswith("bytes")
        print(
            f"check {status} accept-ranges={accept or '-'} range={content_range or '-'} {key}",
            flush=True,
        )
        if not ok:
            failed = True
    if failed:
        raise SystemExit("a sample did not answer 206 with a byte Content-Range")


def main():
    for name in ("CLOUDFLARE_API_TOKEN", "R2_ACCOUNT_ID", "R2_ASSETS_BUCKET"):
        if not os.environ.get(name):
            raise SystemExit(f"missing {name}")
    remote = list_remote()
    files = local_files()
    uploaded = 0
    skipped = 0
    for key, path in files:
        size = path.stat().st_size
        if remote.get(key) == size:
            skipped += 1
            continue
        print(f"upload {key} ({size})", flush=True)
        upload(key, path)
        uploaded += 1
        time.sleep(0.3)
    print(f"done uploaded={uploaded} skipped={skipped} total={len(files)}", flush=True)
    verify(sample_keys(files))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
