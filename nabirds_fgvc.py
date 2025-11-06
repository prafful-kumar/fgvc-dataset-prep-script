import os
import json

# Set path to your NABirds root directory
root_dir = '/home/praful/scratch/petl/fgvc/nabirds'
images_file = os.path.join(root_dir, 'images.txt')
labels_file = os.path.join(root_dir, 'image_class_labels.txt')
split_file = os.path.join(root_dir, 'train_test_split.txt')

# Load UUID → path mapping
id_to_path = {}
with open(images_file, 'r') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 2:
            uuid, path = parts
            id_to_path[uuid] = path

# Load UUID → label (zero-indexed)
id_to_label = {}
with open(labels_file, 'r') as f:
    for line in f:
        uuid, label = line.strip().split()
        id_to_label[uuid] = int(label) - 1

# Load UUID → split (1 = train, 0 = test)
id_to_split = {}
with open(split_file, 'r') as f:
    for line in f:
        uuid, split = line.strip().split()
        id_to_split[uuid] = int(split)

# Build dicts
train_dict = {}
test_dict = {}

for uuid, path in id_to_path.items():
    label = id_to_label[uuid]
    if id_to_split[uuid] == 1:
        train_dict[path] = label
    else:
        test_dict[path] = label

# Write JSON files
with open(os.path.join(root_dir, 'train.json'), 'w') as f:
    json.dump(train_dict, f, indent=2)

with open(os.path.join(root_dir, 'test.json'), 'w') as f:
    json.dump(test_dict, f, indent=2)
