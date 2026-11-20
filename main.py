"""The Daily Ledger, 20 November 2026 -- the entry program.

The page itself is drawn once, at build time, and committed beside this file as
entry.png.  The grader runs this program twice in a sandbox with no network,
and both runs must leave /output/entry.png holding the same bytes, so the
program does nothing but copy the PNG across, verify what it wrote, and report.

MAKEFUN_OUTPUT_DIR stands in for /output when running outside the container:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    """Where the grader wants the image, or the local stand-in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def digest(path):
    """sha256 of a file, read in chunks so a 1 MiB entry is never held twice."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def check_png(path):
    """The gate wants a whole PNG inside the size limits; say why if it is not.

    A judge only ever sees the image, so a truncated file is worse than no
    entry at all: this refuses to emit one rather than let a broken page
    through.  The three things checked are the ones the gate states -- byte
    size, pixel size, and that the file is a complete PNG rather than a
    signature with the body cut off.
    """
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        return f"entry.png is {size} bytes, over the {MAX_BYTES} byte cap"
    with open(path, "rb") as fh:
        head = fh.read(33)
        # A file too short to hold a signature and an IEND is truncated whatever
        # it claims; guard the seek so a stub file reports instead of raising.
        tail = b""
        if size >= 12:
            fh.seek(-12, os.SEEK_END)
            tail = fh.read()
    if len(head) < 8 or not head.startswith(PNG_MAGIC):
        return "entry.png is not a PNG: the signature is wrong"
    if len(head) < 33:
        return f"entry.png is only {size} bytes: the header is cut short"
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        return f"entry.png is {width} by {height}, over the {MAX_SIDE} pixel limit"
    if b"IEND" not in tail:
        return "entry.png has no IEND chunk: the file is truncated"
    return None


def main():
    if not os.path.isfile(SOURCE):
        sys.stderr.write(f"entry.png is missing beside {os.path.basename(__file__)}\n")
        return 1

    problem = check_png(SOURCE)
    if problem:
        sys.stderr.write(problem + "\n")
        return 1

    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    target = os.path.join(outdir, "entry.png")
    shutil.copyfile(SOURCE, target)

    want, got = digest(SOURCE), digest(target)
    if want != got:
        sys.stderr.write("the copy does not match the source\n")
        return 1

    print(f"wrote {target} ({os.path.getsize(target)} bytes, sha256 {want[:16]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
