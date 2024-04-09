import os
import shutil

def move_files_from_subdirs_to_current(dir_path='strategies'):
    """
    Moves all files from subdirectories within the specified directory to the current working directory.
    :param dir_path: Path to the directory containing the subdirectories.
    """
    # Iterate over all items in the specified directory
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)  # Full path to the item

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Iterate over all files in the subdirectory
            for file in os.listdir(item_path):
                file_path = os.path.join(item_path, file)  # Full path to the file

                # Check if the item is a file
                if os.path.isfile(file_path):
                    dest_path = os.path.join(os.getcwd(), file)  # Destination path in the current working directory

                    # Ensure not to overwrite existing files
                    if not os.path.exists(dest_path):
                        shutil.move(file_path, dest_path)
                        print(f"Moved: {file_path} -> {dest_path}")
                    else:
                        print(f"File already exists, not moved: {file}")

# Call the function
move_files_from_subdirs_to_current()
