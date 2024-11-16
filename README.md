### README.md

#### Introduction
This repository contains audio and image assets used for the Ultra Hercules project. Follow the instructions below to add new assets to the repository.

https://www.jsdelivr.com/tools/purge

#### Adding Audio Assets
1. **Directory Structure**: Place audio files in the `assets/audio/` directory.
2. **Supported Formats**: Ensure audio files are in `.mp3` format.
3. **Naming Convention**: Name your audio files as `ultra_hercules_${track_id}.mp3`.

#### Adding Image Assets
1. **Directory Structure**: Place image files in the `assets/images/` directory.
2. **Supported Formats**: Ensure image files are in `.jpg` format.
3. **Naming Convention**: Name your image files as `ultra_hercules_${track_id}.jpg`.

#### Track ID Composition
The track ID is composed of 6 numbers:
- The first two are for the artist (e.g., `01` for Ultra Hercules).
- The second two are for the album (`00` if the track is a single).
- The last two are the rank of the track in the album or the rank of singles if it's a single. The first track should be `01` (not `00`).
