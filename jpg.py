from PIL import Image
import os

def convert_jpeg_to_jpg(folder_path):
    # Ensure the folder path is valid
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file in the folder
    for file_name in files:
        # Check if the file is a JPEG image
        if file_name.lower().endswith('.jpeg'):
            # Construct the full file path
            file_path = os.path.join(folder_path, file_name)

            try:
                # Open the image using Pillow
                with Image.open(file_path) as img:
                    # Generate the output file path with '.jpg' extension
                    output_path = os.path.splitext(file_path)[0] + '.jpg'

                    # Convert and save the image as JPG
                    img.convert('RGB').save(output_path)
                    print(f"Converted: {file_path} -> {output_path}")

                # Optionally, you can remove the original .jpeg file
                # os.remove(file_path)  # Uncomment this line to remove the original file

            except Exception as e:
                print(f"Error converting '{file_path}': {e}")

    print("Conversion completed.")

# Example usage:
folder_path = '/Users/adityadebchowdhury/Desktop/extraction/input '
convert_jpeg_to_jpg(folder_path)
