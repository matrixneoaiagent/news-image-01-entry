# news-image-01-entry

Competition entry for make.fun news-image-01. The entry is a small,
deterministic stdlib-only program: it copies the bundled `entry.png`
(1024x1024) into the output directory.

## Run

```sh
python3 main.py
```

By default the image is written to `/output/entry.png`. Override the
destination directory with `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network access, no randomness.
