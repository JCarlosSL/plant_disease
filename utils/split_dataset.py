import numpy as np
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(ROOT_DIR, '../data')

def split_dataset(datos, train_prop=0.7, val_prop=0.15, test_prop=0.15):
    total_datos = len(datos)
    
    train_size = int(total_datos * train_prop)
    val_size = int(total_datos * val_prop)
    test_size = total_datos - train_size - val_size
    
    # shuffle data
    np.random.shuffle(datos)
    
    # split data
    train_set = datos[:train_size]
    val_set = datos[train_size:train_size+val_size]
    test_set = datos[train_size+val_size:]
    
    return train_set, val_set, test_set

def main():
    print('Splitting dataset...')
    name_data = 'PlantVillage_bgremoved'

    data_dir = os.path.join(root_dir, name_data)
    output_dir = os.path.join(root_dir, 'Potato')

    classes = os.listdir(data_dir)
    for class_ in classes:
        class_dir = os.path.join(data_dir, class_)
        images = os.listdir(class_dir)

        train_set, val_set, test_set = split_dataset(images)
        print('train_set:', len(train_set))
        print('val_set:', len(val_set))
        print('test_set:', len(test_set))

        train_dir = os.path.join(output_dir, 'Train', class_)
        if not os.path.exists(train_dir):
            os.makedirs(train_dir)

        val_dir = os.path.join(output_dir, 'Valid', class_)
        if not os.path.exists(val_dir):
            os.makedirs(val_dir)
        
        test_dir = os.path.join(output_dir, 'Test', class_)
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        # copy images to new directories
        for image in train_set:
            os.rename(os.path.join(class_dir, image), os.path.join(train_dir, image))

        for image in val_set:
            os.rename(os.path.join(class_dir, image), os.path.join(val_dir, image))

        for image in test_set:
            os.rename(os.path.join(class_dir, image), os.path.join(test_dir, image))

if __name__ == '__main__':
    main()