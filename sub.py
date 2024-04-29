import os
from PIL import Image

# Function to list files recursively in a directory
def list_files(directory, extensions):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                file_list.append(os.path.join(root, file))
    return file_list

# Function to rename images and extract subfolder names
def rename_images_and_extract_folders(root_dir, output_folder):
    subfolder_names = set()

    # List of image extensions to consider
    image_extensions = ('.jpg', '.jpeg', '.png')

    # Get all image files recursively from the root directory
    image_files = list_files(root_dir, image_extensions)

    # Iterate over each image file
    for idx, image_path in enumerate(image_files):
        # Open the image
        image = Image.open(image_path)

        # Determine the new filename (renaming from 1 to 10)
        new_filename = f"{idx % 10 + 1}.jpg"

        # Save the image with the new filename
        image.save(os.path.join(output_folder, new_filename))

        # Extract subfolder name from the image path
        subfolder_name = os.path.basename(os.path.dirname(image_path))
        subfolder_names.add(subfolder_name)

    # Write subfolder names to a text file
    with open(os.path.join(output_folder, 'subfolder_names.txt'), 'w') as f:
        for name in sorted(subfolder_names):
            f.write(f"{name}\n")

    print("Image renaming and subfolder extraction complete.")

# Example usage:
root_directory = '/Users/adityadebchowdhury/Desktop/Desktop - Aditya’s MacBook Air/opencv2/Face-Recognition-Attendance-Projects-main/Student_Images'
output_directory = '/Users/adityadebchowdhury/Desktop/extraction/output'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Call the function to rename images and extract subfolder names
rename_images_and_extract_folders(root_directory, output_directory)
