import os
from PIL import Image
from torchvision import transforms

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(ROOT_DIR, '../data')

def augmentate_images(images_by_class=1000, input_dir=None):
    transform = transforms.Compose([
        transforms.RandomResizedCrop(224), # 224 x 224 pixels
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(45),
        transforms.RandomAffine(degrees=0, translate=(0.2, 0.2), scale=(0.8, 1.2)),
    ])

    images_in_class = len(os.listdir(input_dir)) # Number of images in class

    aug_images = images_by_class - images_in_class # Number of images to be augmented
    div_by = aug_images // images_in_class - 1 # Number of images by class to be augmented

    for i, filename in enumerate(os.listdir(input_dir)):
        img = Image.open(os.path.join(input_dir, filename))
        name, ext = os.path.splitext(filename)
                                                                                                                                                                                        
        for j in range(div_by):
            img_transformed = transform(img)
            img_transformed.save(os.path.join(input_dir, name + '_' + str(j) + ext))

def main():
    print('Augmentating images...')
    name_data = 'PlantVillage_bgremoved'
    healthy_dir = os.path.join(root_dir, name_data, 'Potato___healthy')
    print(healthy_dir)

    augmentate_images(images_by_class=100, input_dir=healthy_dir)

if __name__ == '__main__':
    main()
