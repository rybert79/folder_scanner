# folder scanner 

A lightweight command-line tool written in Python to scan directories, analyze file sizes, and identify the largest or smallest files.

## Features

- **Recursive scanning** — scans files across nested directories.
- **Hidden file filtering** — skips files and directories whose names begin with `.`.
- **File size analysis** — displays the largest and smallest files found.
- **Total size calculation** — calculates the combined size of scanned files.
- **Top-N selection** — displays a configurable number of files.
- **Sorting options** — choose between ascending and descending file size order.
- **Human-readable sizes** — formats file sizes into B, KB, MB, and GB.

## Requirements

- Python 3.9+
- No external dependencies

## Usage

```bash
python3 main.py <folder> [-c COUNT] [-p {asc,desc}]
```

### Arguments

| Argument | Description | Default |
|---|---|---|
| `folder` | Directory to scan | Required |
| `-c`, `--count` | Number of files to display (1–10) | `3` |
| `-p`, `--pengurutan` | Sorting order: `asc` or `desc` | `asc` |

### Examples

Scan the Downloads directory:

```bash
python3 main.py ~/Downloads
```

Display the 5 smallest files:

```bash
python3 main.py ~/Downloads -c 5 -p asc
```

Display the 10 largest files:

```bash
python3 main.py ~/Downloads -c 10 -p desc
```

## Example Output

```text
Directory       : /home/user/Downloads
largest files  : video.mp4 : 1.45 GB
smallest files : notes.txt : 500 B
files scanned  : 125
total sized    : 3.72 GB

top 3 files diurut secara descending:
1. video.mp4 : 1.45 GB
2. archive.zip : 820.5 MB
3. backup.tar : 340.12 MB
```

## How It Works

Disk Detective traverses directories recursively using `pathlib`, collects file paths, and retrieves file sizes using `stat().st_size`.

Files are then selected based on their sizes using Python's built-in `min()` and `max()` functions.

## Limitations

- Hidden files and directories are excluded.
- The number of displayed files is limited to 10.
- Filesystem access errors may interrupt scanning.
- File sizes are displayed using decimal units (1 KB = 1,000 bytes).

## License

MIT License
