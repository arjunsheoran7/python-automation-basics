import os

# Folder containing files to rename
TARGET_FOLDER = "sample_folder"

# Base name for renamed files
BASE_NAME = "file"

# Start counter
counter = 1

for file_name in os.listdir(TARGET_FOLDER):
    file_path = os.path.join(TARGET_FOLDER, file_name)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1]
        new_name = f"{BASE_NAME}_{counter}{file_extension}"
        new_path = os.path.join(TARGET_FOLDER, new_name)

        os.rename(file_path, new_path)
        counter += 1
