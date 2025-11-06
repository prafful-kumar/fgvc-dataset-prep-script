import os
import json
from scipy.io import loadmat

def load_dog_split(mat_path):
    mat = loadmat(mat_path)
    file_list = mat['file_list']
    labels = mat['labels'].squeeze()  # shape: (N,)

    result = {}
    for i in range(len(file_list)):
        path = file_list[i][0][0]  # This gets the actual string from the array
        print(path)
        label = int(labels[i]) - 1  # Convert to zero-based
        print(label)
        result[path] = label
    return result

root_dir = '/home/praful/scratch/petl/fgvc/StanfordDogs'

train_dict = load_dog_split(os.path.join(root_dir, 'train_list.mat'))
test_dict = load_dog_split(os.path.join(root_dir, 'test_list.mat'))

with open(os.path.join(root_dir, 'train.json'), 'w') as f:
    json.dump(train_dict, f, indent=2)

with open(os.path.join(root_dir, 'test.json'), 'w') as f:
    json.dump(test_dict, f, indent=2)
