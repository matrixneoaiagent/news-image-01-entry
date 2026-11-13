import os
import shutil
from pathlib import Path

src = Path(__file__).with_name("entry.png")
outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
outdir.mkdir(parents=True, exist_ok=True)
# Copy the bundled 1024x1024 PNG verbatim so the output is byte-identical.
shutil.copyfile(src, outdir / "entry.png")
print(outdir / "entry.png")
