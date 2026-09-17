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

remain : https://www.youtube.com/watch?v=JvMtIe2Ojd4 7arb L`Mic - HOSPITAL UNDERGROUND Feat. ZANKA FLOW
https://www.youtube.com/watch?v=Mh9W4QbMwzQ LYRICS MANTSAYADCH - Muslim & Shayfeen & Dizzy Dros & Ahmed Soultan by DJ Van
https://www.youtube.com/watch?v=Ufsj0SBkge4 Muslim - Aka Rap - Compilation Dj Cut Killer 2008
https://www.youtube.com/watch?v=gEecI-ZqPsY Muslim - Edounya 7ekmet (Feat. Islamic Gun) 2005 الدنيا حكمت
 https://www.youtube.com/watch?v=89qANCJCJR0 Zanka Flow ( Muslim & L3arbé ) - 7naychen Part I - Compilation 9amouss Zna9i
https://www.youtube.com/watch?v=K1SSMGOgHAo Zanka Flow (Muslim & L3arbé) - Flow Dbaa7 2008
https://www.youtube.com/watch?v=zkVC2ojlefE Askri Dlam Feat. Muslim - RRawda 2005 الرَّوضة
https://www.youtube.com/watch?v=EO_j1VhFWqM Style Souss Feat. Muslim - Nifa9 (نفاق)
https://www.youtube.com/watch?v=SyRqeSlIjt4 Chagrin Éternel - Islamic Gun Feat. Muslim -2003- Compilation Positive School
https://www.youtube.com/watch?v=N1O8_i_VJlY KaCheLa & Pen Power - 18 juin
https://www.youtube.com/watch?v=ySdzs5WV2fA KaCheLa & Pen Power - FreeStyle Msskoun
https://www.youtube.com/watch?v=VJYvS49OQZs Casa Crew Feat. Zanka Flow - Klam Rejal
https://www.youtube.com/watch?v=Kx6G_EYtnz0 Tanjawa Daba - Vol.2 - Compilation Positive School 2002
https://www.youtube.com/watch?v=Fm3HnUlnuzc 16 - Muslim - Lkhawa Dyali مسلم ـ الخـاوا ديـالي
https://www.youtube.com/watch?v=89qANCJCJR0 Zanka Flow ( Muslim & L3arbé ) - 7naychen Part I - Compilation 9amouss Zna9i


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
