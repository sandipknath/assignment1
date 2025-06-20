import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination directory exists
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    # List all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)

        # Skip subdirectories, only back up files
        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_dir, filename)

            # Check if file already exists in destination
            if os.path.exists(dest_file):
                # Append timestamp to filename
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_dir, new_filename)

            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {filename} -> {os.path.basename(dest_file)}")
            except Exception as e:
                print(f"Failed to copy {filename}: {e}")

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source = sys.argv[1]
        destination = sys.argv[2]
        backup_files(source, destination)
