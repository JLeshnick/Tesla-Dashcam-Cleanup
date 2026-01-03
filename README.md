# TeslaCam Sentry Reviewer & Cleaner

A Python toolkit to efficiently clean up "junk" Tesla Sentry Mode clips (rain, wind, lights, etc.) from your USB drive. 

Instead of opening hundreds of folders one by one, this tool extracts all event thumbnails into a single folder. You can visually scan them, delete the ones you don't want, and let the script automatically delete the corresponding massive video folders.

## Features
* **Mass Thumbnail Extraction:** Pulls `thumb.png` from all event folders into a single review directory.
* **Slow-Drive Safe:** Includes "Force Find" logic to handle lagging external hard drives that might otherwise hide files.
* **Smart Cleanup:** Syncs your thumbnail deletions to the actual video folders.
* **Safety First:** double-checks for video files before deleting "empty" folders and requires two confirmation steps before deleting any data.

## Prerequisites
* [Python 3.x](https://www.python.org/downloads/) installed.

## Setup
1.  Clone or download this repository.
2.  Open the scripts (`thumbnail-review.py` and `cleanup.py`) in a text editor (Notepad, VS Code, etc.).
3.  Edit the **Configuration** section at the top of both files to match your drive letter:

```python
# --- CONFIGURATION ---
source_dir = r"D:\TeslaCam\SentryClips"       # Path to your Tesla Drive
review_dir = r"D:\TeslaCam\_Thumbnail_Review" # Where you want thumbnails to go
# ---------------------