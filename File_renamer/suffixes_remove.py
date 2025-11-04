# Author: Kurath
# Date: 2026-03-15
# Purpose: This script removes a editable suffix from filenames in its directory.
import os

script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path)
script_filename = os.path.basename(script_path)
suffix_to_remove = '[undealed]'
print(f"starting to deal with the folder: {folder_path}")

try:
    filenames = os.listdir(folder_path)
except FileNotFoundError:
    print(f"The folder {folder_path} does not exist.")
    filenames = []
except NotADirectoryError:
    print(f"The path {folder_path} is not a directory.")
    filenames = []
count = 0
for filename in filenames:
    if filename == script_filename:
        print(f"Skipping the script file itself: {filename}")
        continue
    old_path = os.path.join(folder_path, filename)
    if os.path.isfile(old_path):
        if filename.endswith(suffix_to_remove):
            new_filename = filename[:-len(suffix_to_remove)]
            new_path = os.path.join(folder_path, new_filename)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
                count += 1
            except FileExistsError:
                print(f"Cannot rename {old_path} to {new_path}: target file already exists.")
            except OSError as e:
                print(f"Error renaming {old_path} to {new_path}: {e}")
    else:
        print(f"Skipping {old_path}: not a file.")
print(f"Total files renamed: {count}")