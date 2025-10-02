import os

folder_path = 'images/'
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(filename)

from PIL import Image

with Image.open('images/sample.jpg') as img:
    resized_img = img.resize((800, 600))  # Resize to 800x600
    resized_img.save('output/sample_resized.jpg', 'JPEG')

import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), output_format='JPEG'):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(input_folder, filename)
            with Image.open(filepath) as img:
                resized = img.resize(size)
                
                # Clean filename
                name, _ = os.path.splitext(filename)
                output_path = os.path.join(output_folder, f"{name}.{output_format.lower()}")
                
                resized.save(output_path, output_format)
                print(f"Saved: {output_path}")

# Example usage
resize_images('images', 'resized_images', size=(800, 600), output_format='JPEG')
