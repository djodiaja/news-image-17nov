"""Entry for the make.fun news-image-20261117 bounty.

Writes a pre-rendered infographic summarizing 17 November 2026 world news
to the output directory. The image is checked in as entry.png in this repo.
The script is deterministic: two runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    repo_dir = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_dir / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
