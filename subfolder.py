import os
import shutil

def organize_files(source_dir):
    # List all files in the source directory
    files = os.listdir(source_dir)

    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            # Get the file extension
            _, ext = os.path.splitext(file)

            # Create a folder based on the file name (excluding extension)
            folder_name = file.replace(ext, '').strip()
            folder_path = os.path.join(source_dir, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file into the corresponding folder
            file_path = os.path.join(source_dir, file)
            shutil.move(file_path, folder_path)

if __name__ == "__main__":
    # Specify the source directory where files are located
    source_directory = '/Users/adityadebchowdhury/Desktop/extraction/input /BCA 4'

    # Call the function to organize files
    organize_files(source_directory)

    print("Files organized into subfolders based on names.")
