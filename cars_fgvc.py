import os
import json
from scipy.io import loadmat

# Paths
root_dir = '/home/praful/scratch/petl/fgvc/StanfordCars'
devkit_dir = os.path.join(root_dir, 'car_devkit/devkit')

# Load training annotations
def load_train_split(mat_path, img_dir):
    mat = loadmat(mat_path)
    annos = mat['annotations'][0]
    result = {}
    for entry in annos:
        fname = entry['fname'][0]
        label = int(entry['class'][0][0]) - 1  # Convert to 0-based
        result[os.path.join(img_dir, fname)] = label
    return result

# Load test annotations (no labels)
def load_test_split(mat_path, img_dir):
    mat = loadmat(mat_path)
    print(mat.keys())
    annos = mat['annotations'][0]
    print(annos)
    return [os.path.join(img_dir, entry['fname'][0]) for entry in annos]

# Generate dictionaries
train_json = load_train_split(os.path.join(devkit_dir, 'cars_train_annos.mat'), 'cars_train')
# test_json = load_test_split(os.path.join(devkit_dir, 'cars_test_annos.mat'), 'cars_test')
test_json = load_train_split(os.path.join(devkit_dir, 'cars_test_annos_withlabels.mat'), 'cars_test')
# Save JSONs
with open(os.path.join(root_dir, 'train.json'), 'w') as f:
    json.dump(train_json, f, indent=2)

with open(os.path.join(root_dir, 'test.json'), 'w') as f:
    json.dump(test_json, f, indent=2)

print(f"train.json with {len(train_json)} entries saved.")
print(f"test.json with {len(test_json)} entries saved.")
