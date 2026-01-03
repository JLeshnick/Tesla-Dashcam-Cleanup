# TeslaCam Sentry Clips Cleanup Tool

A Python toolkit to efficiently clean up "junk" Tesla Sentry Mode clips (rain, wind, empty garages) from your USB drive.

**The Problem:** Tesla saves events in separate folders. Checking them one by one is slow.

**The Solution:** This tool extracts all event thumbnails into a single folder. You simply look at the pictures, delete the ones that show nothing interesting, and the tool will automatically delete the corresponding massive video folders for you.

## ⚠️ Important Warning
**This tool permanently deletes files.**
While safety features are included (confirmation prompts, protected folders), you should always double-check your drive before confirming the final deletion.

---

## 🛠️ Prerequisites

1.  **Install Python:**
    * Download Python from [python.org](https://www.python.org/downloads/).
    * **CRITICAL:** During installation, check the box that says **"Add Python to PATH"**.

2.  **Download this Tool:**
    * Click the green **Code** button above and select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer (e.g., `Documents\TeslaCamTools`).

---

## ⚙️ Configuration (Do this first!)

Before running anything, you need to tell the scripts where your Tesla USB drive is located.

1.  Plug in your Tesla USB drive. Check which drive letter it was assigned (e.g., `D:`, `E:`, `F:`).
2.  Right-click `thumbnail-review.py` and select **Edit with Notepad** (or any text editor).
3.  Look for the configuration section at the top:
    ```python
    # --- CONFIGURATION ---
    source_dir = r"D:\TeslaCam\SentryClips"       # <--- CHANGE "D" to your drive letter
    review_dir = r"D:\TeslaCam\_Thumbnail_Review" # <--- You can leave this as is
    # ---------------------
    ```
4.  Update the `D:` to match your USB drive letter.
5.  Save the file.
6.  **Repeat steps 2-5** for the file `cleanup.py`.

---

## 🚀 Step-by-Step Usage Guide

### Step 1: Extract Thumbnails
This script scans your drive and copies the `thumb.png` from every event into a single folder. It includes "Force Find" logic to handle slow or lagging mechanical hard drives.

1.  Open the folder where you saved these scripts.
2.  Type `cmd` in the address bar at the top of the File Explorer window and hit **Enter**. (This opens a black command terminal).
3.  In the terminal, type the following and hit **Enter**:
    ```bash
    python thumbnail_review.py
    ```
4.  Wait for the process to finish. It will tell you how many thumbnails were extracted.

### Step 2: The Visual Review (The "Culling")
This is where you decide what to keep.

1.  Open your review folder (default: `D:\TeslaCam\_Thumbnail_Review`).
2.  In File Explorer, go to the **View** tab and select **Extra Large Icons**.
3.  Scroll through the images.
4.  **Delete the thumbnails** for any events you want to **REMOVE** from your drive (e.g., rain, empty garage, trees blowing).
    * **Keep the thumbnail** = Keep the video.
    * **Delete the thumbnail** = The video will be deleted in the next step.

### Step 3: Cleanup
Now we sync your changes. This script looks at which thumbnails are left and deletes the video folders for the ones you removed.

1.  Go back to your terminal window (or open a new one as described in Step 1).
2.  Type the following and hit **Enter**:
    ```bash
    python cleanup.py
    ```
3.  **Review the Report:** The script will list exactly which folders are about to be deleted and the total file size.
4.  **Confirm:**
    * Type `DELETE` (all caps) when prompted to confirm the list.
    * Type `YES` (all caps) to confirm the final deletion.

---

## ❓ Troubleshooting

**The extraction script is missing files!**
If your drive is under heavy load (e.g., you are copying files to it while running this), the script might miss files.
* **Solution:** Stop all other file transfers. Wait 2 minutes for the drive to settle. Run `python thumbnail-review.py` again. It will pick up the missing items.

**I see "[PROTECTED]" folders in the cleanup report.**
This means the script found a folder that had video files but **no** thumbnail in your review list.
* **Cause:** Usually a corrupt save by the car, or you accidentally deleted a thumbnail for a valid clip.
* **Action:** The script will **SKIP** these automatically to be safe. You should check these folders manually on the drive.
