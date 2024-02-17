from rembg import remove
import cv2
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(ROOT_DIR, '../data')

def remove_background(image):
    image = cv2.imread(image)
    image = remove(image, alpha_matte=True, alpha_matte_erode_size=2)
    return image


def remove_background_from_images(input_dir, output_dir):
    for subdir, dirs, files in os.walk(input_dir):
        for file in files:
            image = os.path.join(subdir, file)
            image = remove_background(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            new_dir = subdir.replace(input_dir, output_dir)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            cv2.imwrite(os.path.join(new_dir, file), image)

def main():
    print('Removing background from images...')
    print('root_dir:', root_dir)

    name_data = 'PlantVillage'

    test_dir = os.path.join(root_dir, name_data, 'Potato___healthy')
    test_output_dir = os.path.join(root_dir, f'{name_data}_bgremoved', 'Potato___healthy')
    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)
    remove_background_from_images(test_dir, test_output_dir)

if __name__ == '__main__':
    main()