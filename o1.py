import dlib
import cv2
import numpy as np
import os

def extract_faces_high_accuracy(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize the face detector (MMOD) from dlib
    detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

    # Loop over all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct the file path
        filepath = os.path.join(input_folder, filename)

        # Check if the file is a valid image file (JPEG, PNG, JPG)
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load the input image using OpenCV
            image = cv2.imread(filepath)

            if image is None:
                print(f"Error: Unable to read '{filepath}'. Skipping.")
                continue

            # Convert the image to RGB (dlib requires RGB format)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Detect faces in the RGB image using dlib's MMOD detector
            faces = detector(image_rgb, 1)

            # Iterate over detected faces
            for i, face in enumerate(faces):
                # Extract the face region from the image
                x1 = face.rect.left()
                y1 = face.rect.top()
                x2 = face.rect.right()
                y2 = face.rect.bottom()

                # Ensure the extracted region is within the image bounds
                x1, y1 = max(x1, 0), max(y1, 0)
                x2, y2 = min(x2, image.shape[1]), min(y2, image.shape[0])

                # Extract the face ROI (Region of Interest)
                face_roi = image[y1:y2, x1:x2]

                # Save the extracted face as a new image in the output folder
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i+1}.jpg")
                cv2.imwrite(output_path, face_roi)

                print(f"Face {i+1} extracted from '{filename}' and saved as '{output_path}'.")

# Example usage:
input_folder = "/Users/adityadebchowdhury/Desktop/extraction/input /BCA 4"
output_folder = "/Users/adityadebchowdhury/Desktop/extraction/output2"
extract_faces_high_accuracy(input_folder, output_folder)
