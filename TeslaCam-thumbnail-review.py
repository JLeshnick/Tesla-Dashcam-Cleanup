import os
import shutil

# --- CONFIGURATION ---
source_dir = r"D:\TeslaCam\SentryClips"
review_dir = r"D:\TeslaCam\_Thumbnail_Review"
# ---------------------

def extract_thumbnails():
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found.")
        return

    # Create the review directory if it doesn't exist
    if not os.path.exists(review_dir):
        os.makedirs(review_dir)
        print(f"Created review folder at: {review_dir}")

    count = 0
    print("Scanning folders...")

    # Walk through all directories in source_dir
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file == "thumb.png":
                # Get the name of the folder containing the event (e.g., 2025-12-30_16-38-00)
                event_folder_name = os.path.basename(root)
                
                # Construct new filename: EventName_thumb.png
                new_filename = f"{event_folder_name}_thumb.png"
                
                source_path = os.path.join(root, file)
                dest_path = os.path.join(review_dir, new_filename)

                # Copy the file
                shutil.copy2(source_path, dest_path)
                count += 1
                
    print(f"Done! Extracted {count} thumbnails to '{review_dir}'")

if __name__ == "__main__":
    extract_thumbnails()