# news-image-20261127-a — Front Page Classic

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/prellxz-gm/news-image-20261127-a/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/prellxz-gm/news-image-20261127-a/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A dense but legible newspaper front page summing up **Friday 27 November 2026** in
one image. Hero: tankers ablaze in the Strait of Hormuz after hitting naval
mines. Below it, the IRGC warning shots at a US F-16 escorting tankers SE of
Hengam Island and Brent crude near the month's high, then a region-grouped day-in-brief band covering all 25 verified
stories from 9 regions — plus a DATE CHECK row that names the traps (Macy's
parade postponement = 26 Nov, Cairo tanker fire = 25 Nov) so they are never
drawn as 27-Nov news.

The image is pre-rendered with PIL (see the build script in the author's
workspace, not shipped here); `main.py` is a stdlib-only copy program that
places `entry.png` into the output directory.

## Run it

```sh
python3 main.py
```

This writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`) and
verifies the copy is byte-identical to the shipped image and starts with the
PNG magic bytes.

<sub>Entered on [make.fun](https://make.fun/?ref=jyrqfb5w&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
