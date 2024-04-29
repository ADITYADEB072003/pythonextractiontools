import cv2
import os

# Path to the directory containing student images
input_path = '/Users/adityadebchowdhury/Desktop/Desktop - Aditya’s MacBook Air/opencv2/Face-Recognition-Attendance-Projects-main/Student_Images'
desired_width = 420  # Desired width of resized images
desired_height = 640  # Desired height of resized images

def resize_images_in_place(input_folder, width, height):
    """
    Resize all images in the input folder to the specified width and height,
    and overwrite the original images with the resized versions.
    """
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                input_file_path = os.path.join(root, file)

                # Read and resize the image
                img = cv2.imread(input_file_path)
                if img is not None:
                    resized_img = cv2.resize(img, (width, height))
                    cv2.imwrite(input_file_path, resized_img)
                    print(f"Resized and overwritten: {input_file_path}")
                else:
                    print(f"Error: Unable to read image {input_file_path}")

# Resize images in the input folder in-place
resize_images_in_place(input_path, desired_width, desired_height)

print("Batch resizing complete.")
