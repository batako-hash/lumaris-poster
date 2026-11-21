#!/usr/bin/env python3
"""Write the LUMARIS poster to the competition output file.

Reads entry.png from the same directory as this script and writes those
exact bytes to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
The file is a whole JPEG of 220,728 bytes at 1024x1024 pixels: within the
gate of at most 1 MiB and at most 1024 by 1024 pixels. The checks run
before anything is written, and the copy is verified byte-for-byte after
writing, so two runs produce identical output.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1048576
MAX_DIMENSION = 1024

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from the first SOF marker of a JPEG file."""
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG file")
    pos = 2
    while pos + 9 < len(data):
        if data[pos] != 0xFF:
            raise ValueError("corrupt JPEG marker stream")
        marker = data[pos + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        size = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + size
    raise ValueError("no SOF marker found in JPEG")


def png_dimensions(data: bytes) -> tuple[int, int]:
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    here = Path(__file__).resolve().parent
    image_path = here / "entry.png"
    data = image_path.read_bytes()
    size = len(data)
    if size == 0 or size > MAX_BYTES:
        print(
            f"entry.png is {size} bytes; must be between 1 and {MAX_BYTES}.",
            file=sys.stderr,
        )
        return 1
    if data[:8] == PNG_MAGIC:
        kind = "PNG"
        width, height = png_dimensions(data)
    elif data[:3] == JPEG_MAGIC:
        kind = "JPEG"
        width, height = jpeg_dimensions(data)
    else:
        print("entry.png is neither a PNG nor a JPEG.", file=sys.stderr)
        return 1
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(
            f"entry.png is {width}x{height}; "
            f"must be at most {MAX_DIMENSION}x{MAX_DIMENSION}.",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.png"
    out_path.write_bytes(data)
    written = out_path.read_bytes()
    if written != data:
        print(f"verification failed: {out_path} does not match entry.png",
              file=sys.stderr)
        return 1
    print(f"wrote {kind} {size} bytes ({width}x{height}) "
          f"sha256={hashlib.sha256(data).hexdigest()} to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
