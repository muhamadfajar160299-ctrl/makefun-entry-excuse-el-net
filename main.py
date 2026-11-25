"""Write the one-line entry to the grader output directory.

Reads entry.txt next to this file and writes it byte-identical to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output), mode 0644,
with a single direct write and no temporary file or rename.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _write_once(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    data = (HERE / "entry.txt").read_bytes()
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)


def main():
    try:
        _write_once(Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"))
    except OSError:
        _write_once(Path("/output"))


if __name__ == "__main__":
    main()
