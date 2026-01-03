import os
import shutil
import time

# --- CONFIGURATION ---
source_dir = r"D:\TeslaCam\SentryClips"
review_dir = r"D:\TeslaCam\_Thumbnail_Review"
# ---------------------

def force_extract():
    if not os.path.exists(review_dir):
        os.makedirs(review_dir)

    print(f"Scanning {source_dir}...")
    print("Mode: AGGRESSIVE RE-CHECK (For busy/slow drives)\n")

    copied_count = 0
    recovered_count = 0

    for root, dirs, files in os.walk(source_dir):
        if "_Thumbnail_Review" in root:
            continue

        # Check if we already have this one (Skip fast)
        event_folder_name = os.path.basename(root)
        dest_filename = f"{event_folder_name}_thumb.png"
        dest_path = os.path.join(review_dir, dest_filename)
        
        if os.path.exists(dest_path):
            continue

        # 1. Standard Check: Is it in the list?
        thumb_candidates = [f for f in files if f.lower() == "thumb.png"]

        # 2. FORCE CHECK: If not in list, force the OS to look for the specific path
        if not thumb_candidates:
            # Construct the theoretical path
            potential_thumb_path = os.path.join(root, "thumb.png")
            
            # Check up to 3 times with delays
            for attempt in range(1, 4):
                if os.path.exists(potential_thumb_path):
                    # We found it by force!
                    thumb_candidates = ["thumb.png"] # Fake the list entry
                    recovered_count += 1
                    print(f"   [Recovered] Drive hid '{event_folder_name}/thumb.png' but we found it on retry {attempt}.")
                    break
                
                # If this folder has video files, it SHOULD have a thumb. Wait and try again.
                # (We check for .mp4 to ensure we aren't waiting on empty junk folders)
                has_video = any(f.lower().endswith('.mp4') for f in files)
                if has_video:
                    time.sleep(1.0) # Wait 1 second
                else:
                    break # If no video files, don't waste time waiting.

        # 3. Copy if found
        if thumb_candidates:
            source_path = os.path.join(root, thumb_candidates[0])
            try:
                # 0KB Check
                if os.path.getsize(source_path) > 0:
                    shutil.copy2(source_path, dest_path)
                    copied_count += 1
                    if copied_count % 20 == 0:
                        print(f"   ... Extracted {copied_count} ...")
            except Exception as e:
                print(f"[Error] Failed to copy from {event_folder_name}: {e}")

    print("\n" + "="*40)
    print(f"Extraction Complete!")
    print(f"New Thumbnails: {copied_count}")
    print(f"Recovered from lag: {recovered_count}")
    print("="*40)

if __name__ == "__main__":
    force_extract()