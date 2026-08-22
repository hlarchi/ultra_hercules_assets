### README.md

#### Introduction

This repository contains audio and image assets used for the Ultra Hercules
project. Follow the instructions below to add new assets to the repository.

https://www.jsdelivr.com/tools/purge :
https://cdn.jsdelivr.net/gh/hlarchi/ultra_hercules_assets@main/img/social/covers/amirl9wafi.jpg

#### Adding Audio Assets

1. **Directory Structure**: Place audio files in the `assets/audio/` directory.
2. **Supported Formats**: Ensure audio files are in `.mp3` format.
3. **Naming Convention**: Name your audio files as
   `ultra_hercules_${track_id}.mp3`.

#### Adding Image Assets

1. **Directory Structure**: Place image files in the `assets/images/` directory.
2. **Supported Formats**: Ensure image files are in `.jpg` format.
3. **Naming Convention**: Name your image files as
   `ultra_hercules_${track_id}.jpg`.

#### Track ID Composition

The track ID is composed of 6 numbers:

- The first two are for the artist (e.g., `01` for Ultra Hercules).
- The second two are for the album (`00` if the track is a single).
- The last two are the rank of the track in the album or the rank of singles if
  it's a single. The first track should be `01` (not `00`).

to analyse music quality check : https://academo.org/demos/spectrum-analyzer/

to downlaoad from spotify : https://spotidown.app/en1 or https://spotdown.org/fr

to download from youtube : https://ssyoutube.is/convert/

from apple music : https://aaplmusicdownloader.com/

remain : https://www.youtube.com/watch?v=JrRBRy_ZbZQ Ch3andek Ft Dj AFRICANO
https://www.youtube.com/watch?v=1OkXaiBNfFc Caballero
https://www.youtube.com/watch?v=9X3xSrWHJQM My Lady
https://www.youtube.com/watch?v=fWMaCMujKrw Lwada3 a Sahbi (Reprise)
https://www.youtube.com/watch?v=NaVD4Uj9OY8 Skati
https://www.youtube.com/watch?v=gQ23txdLjRg 7NAYA
https://www.youtube.com/watch?v=nppv2VXd9dQ SERREK
https://www.youtube.com/watch?v=ozLfzQ21RIw JLWK
https://www.youtube.com/watch?v=-k-UwO4nW2Y RMADI
https://www.youtube.com/watch?v=Q-X-dS_tfyA Berrani
https://www.youtube.com/watch?v=_aW3YsRDxIU Khamri
https://www.youtube.com/watch?v=ThY7PavylIM Lkhayal
https://www.youtube.com/watch?v=8cgePyXuO04 Zahri

mkdir -p /Users/hlarchi/Downloads/opus && yt-dlp --no-warnings --extractor-args
"youtube:player_client=android,web" -f "bestaudio/ba/b" -x --audio-format opus
--no-embed-thumbnail -o "/Users/hlarchi/Downloads/opus/%(title)s.%(ext)s"\
"https://www.youtube.com/watch?v=JrRBRy_ZbZQ"\
"https://www.youtube.com/watch?v=1OkXaiBNfFc"\
"https://www.youtube.com/watch?v=9X3xSrWHJQM"\
"https://www.youtube.com/watch?v=fWMaCMujKrw"\
"https://www.youtube.com/watch?v=NaVD4Uj9OY8"\
"https://www.youtube.com/watch?v=gQ23txdLjRg"\
"https://www.youtube.com/watch?v=nppv2VXd9dQ"\
"https://www.youtube.com/watch?v=ozLfzQ21RIw"\
"https://www.youtube.com/watch?v=-k-UwO4nW2Y"\
"https://www.youtube.com/watch?v=Q-X-dS_tfyA"\
"https://www.youtube.com/watch?v=_aW3YsRDxIU"\
"https://www.youtube.com/watch?v=ThY7PavylIM"\
"https://www.youtube.com/watch?v=8cgePyXuO04"

for f in /Users/hlarchi/Downloads/opus/_.opus; do ffmpeg -i
"$f" -c:a aac_at -b:a 160k "${f%._}.m4a" && rm "$f"; done
