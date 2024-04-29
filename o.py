import cv2
import dlib
import os

def extract_faces_from_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize the face detector (HOG-based) and the facial landmark predictor
    detector = dlib.get_frontal_face_detector()

    # Loop over all files in the input folder
    for filename in os.listdir(input_folder):
        # Construct the file path
        filepath = os.path.join(input_folder, filename)

        # Check if the file is a valid image file (JPEG or PNG)
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load the input image using OpenCV
            image = cv2.imread(filepath)

            if image is None:
                print(f"Error: Unable to read '{filepath}'. Skipping.")
                continue

            # Convert the image to grayscale for face detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale image
            faces = detector(gray)

            if len(faces) == 0:
                print(f"No faces detected in '{filepath}'. Skipping.")
                continue

            # Iterate over detected faces
            for i, face in enumerate(faces):
                # Extract the face region from the image
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                
                # Ensure the extracted region is within the image bounds
                x1, y1 = max(x, 0), max(y, 0)
                x2, y2 = min(x + w, image.shape[1]), min(y + h, image.shape[0])

                # Extract the face ROI (Region of Interest)
                face_roi = image[y1:y2, x1:x2]

                # Save the extracted face as a new image in the output folder
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_face_{i+1}.jpg")
                cv2.imwrite(output_path, face_roi)

                print(f"Face {i+1} extracted from '{filename}' and saved as '{output_path}'.")

# Example usage:
input_folder = '/Users/adityadebchowdhury/Desktop/extraction/input '
output_folder = '/Users/adityadebchowdhury/Desktop/extraction/output'
extract_faces_from_folder(input_folder, output_folder)
