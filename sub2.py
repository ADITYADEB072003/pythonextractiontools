import os

# Function to rename files within each subfolder and extract subfolder names
def rename_files_and_extract_folders(root_dir):
    subfolder_names = set()

    # Iterate over each subfolder in the root directory
    for subdir, _, files in os.walk(root_dir):
        if files:
            # Extract subfolder name
            subfolder_name = os.path.basename(subdir)
            subfolder_names.add(subfolder_name)

            # Counter for renaming files within the subfolder
            file_counter = 1

            # Iterate over each file in the subfolder
            for file in files:
                # Ignore non-image files
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Build the original and new file paths
                    old_path = os.path.join(subdir, file)
                    new_filename = f"{file_counter}.jpg"
                    new_path = os.path.join(subdir, new_filename)

                    # Rename the file
                    os.rename(old_path, new_path)

                    # Increment file counter for the next file
                    file_counter += 1

    # Write subfolder names to a text file
    with open(os.path.join(root_dir, 'subfolder_names.txt'), 'w') as f:
        for name in sorted(subfolder_names):
            f.write(f"{name}\n")

    print("File renaming and subfolder extraction complete.")

# Example usage:
root_directory =  '/Users/adityadebchowdhury/Desktop/faceapi/labels'
# Call the function to rename files and extract subfolder names
rename_files_and_extract_folders(root_directory)
