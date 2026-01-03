import os
import shutil
import math  # <--- Added this missing import

# --- CONFIGURATION ---
source_dir = r"D:\TeslaCam\SentryClips"
review_dir = r"D:\TeslaCam\_Thumbnail_Review"
# ---------------------

def get_dir_size(path):
    """Calculates the total size of a directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size_bytes):
    """Converts bytes to human readable string (GB/MB)."""
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.log(size_bytes, 1024))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def main():
    if not os.path.exists(review_dir):
        print("Error: Review directory not found. Have you extracted thumbnails yet?")
        return

    print("Analyzing folders... this may take a moment to calculate sizes...")

    # 1. Get the list of "Keepers" based on thumbnails remaining
    kept_thumbnails = [f for f in os.listdir(review_dir) if f.endswith("thumb.png")]
    kept_event_names = {name.replace("_thumb.png", "") for name in kept_thumbnails}

    folders_to_keep = []
    folders_to_delete = []
    total_delete_size = 0

    # 2. Sort folders into Keep vs Delete lists
    for event_folder in sorted(os.listdir(source_dir)):
        event_path = os.path.join(source_dir, event_folder)
        
        if os.path.isdir(event_path):
            if event_folder in kept_event_names:
                folders_to_keep.append(event_folder)
            else:
                # Calculate size before adding to list
                size = get_dir_size(event_path)
                total_delete_size += size
                folders_to_delete.append(event_folder)

    # --- REPORTING ---
    print("\n" + "="*40)
    print(f"   ANALYSIS REPORT")
    print("="*40)
    
    print(f"\n--- FOLDERS TO BE KEPT ({len(folders_to_keep)}) ---")
    # Only printing the count to keep the console clean, remove comment to print all
    # for f in folders_to_keep: print(f" [KEEP] {f}")
    print(f" (List hidden to save space, but {len(folders_to_keep)} folders are safe)")

    print(f"\n--- FOLDERS TO BE DELETED ({len(folders_to_delete)}) ---")
    if len(folders_to_delete) > 0:
        for f in folders_to_delete:
            print(f" [DELETE] {f}")
    else:
        print(" No folders to delete. You are safe.")
        return

    formatted_size = format_size(total_delete_size)
    print("\n" + "="*40)
    print(f"TOTAL DATA TO DELETE: {formatted_size}")
    print("="*40)

    # --- CONFIRMATION 1 ---
    print("\nWARNING: The folders listed above under [DELETE] will be permanently removed.")
    print("This cannot be undone.")
    confirm1 = input(f"Type 'DELETE' (all caps) to confirm deletion of {len(folders_to_delete)} folders: ")

    if confirm1 != "DELETE":
        print("\nOperation ABORTED. No files were touched.")
        return

    # --- CONFIRMATION 2 ---
    confirm2 = input(f"FINAL CONFIRMATION: Are you sure you want to reclaim {formatted_size}? Type 'YES': ")

    if confirm2 != "YES":
        print("\nOperation ABORTED. No files were touched.")
        return

    # --- EXECUTION ---
    print("\nStarting deletion...")
    deleted_count = 0
    for folder in folders_to_delete:
        full_path = os.path.join(source_dir, folder)
        try:
            shutil.rmtree(full_path)
            print(f"Deleted: {folder}")
            deleted_count += 1
        except Exception as e:
            print(f"Error deleting {folder}: {e}")

    print("\n" + "="*40)
    print(f"Done. Successfully deleted {deleted_count} folders.")
    print(f"Reclaimed {formatted_size} of space.")

if __name__ == "__main__":
    main()