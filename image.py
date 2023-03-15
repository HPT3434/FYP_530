from PIL import Image
import os

def resize_image(input_path, output_path, size):
    for file_name in os.listdir(input_path):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            input_image_path = os.path.join(input_path, file_name)
            output_image_path = os.path.join(output_path, file_name)
            original_image = Image.open(input_image_path)
            width, height = original_image.size
            print(f"The original image size of {file_name} is {width} wide x {height} high")

            resized_image = original_image.resize(size)
            width, height = resized_image.size
            print(f"The resized image size of {file_name} is {width} wide x {height} high")

            resized_image.save(output_image_path)

if __name__ == '__main__':
    input_path = 'img'
    output_path = 'img/resize'
    size = (640, 640)
    resize_image(input_path, output_path, size)