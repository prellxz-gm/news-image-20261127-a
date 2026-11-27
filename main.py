#!/usr/bin/env python3
"""news-image-20261127 variant A — 'Front Page Classic, precision'.

Copies the pre-rendered front-page image (entry.png, shipped next to this
file) into the grader output directory. Standard library only, fully
deterministic: the same bytes come out on every run.
"""
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_MAGIC):
        print("error: output is not a PNG file", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        original = f.read()
    if data != original:
        print("error: output differs from entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
