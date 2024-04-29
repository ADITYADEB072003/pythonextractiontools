from PIL import Image
import os

input_folder = "/Users/adityadebchowdhury/Desktop/Face-Recognition-Attendance-Projects-main/Training_images"
output_folder = "/Users/adityadebchowdhury/Desktop/extraction/output"
size = (300, 300)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        image = Image.open(os.path.join(input_folder, file_name))
        image.thumbnail(size)
        image.save(os.path.join(output_folder, file_name))