import os
import cv2
from mtcnn import MTCNN

def detect_and_display_faces(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Initialize MTCNN for face detection
    detector = MTCNN()

    # Detect faces in the image
    faces = detector.detect_faces(img)

    # Draw bounding boxes around detected faces
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Draw rectangle
        cv2.putText(img, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)  # Add label

    # Display the image with detected faces
    cv2.imshow('Faces Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_images_in_folder(folder_path):
    # Traverse all subdirectories and process images
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                print(f"Processing image: {image_path}")
                detect_and_display_faces(image_path)

def main():
    folder_path = '/Users/adityadebchowdhury/Desktop/extraction/input /BCA 4'  # Specify the path to the folder containing subfolders with images
    process_images_in_folder(folder_path)

if __name__ == '__main__':
    main()
