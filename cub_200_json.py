import os
import json

root_dir = '/home/praful/scratch/petl/fgvc/CUB_200_2011'
images_file = os.path.join(root_dir, 'images.txt')
labels_file = os.path.join(root_dir, 'image_class_labels.txt')
split_file = os.path.join(root_dir, 'train_test_split.txt')

# Load metadata
with open(images_file, 'r') as f:
    id_to_path = {int(line.split()[0]): line.split()[1] for line in f}

with open(labels_file, 'r') as f:
    id_to_label = {int(line.split()[0]): int(line.split()[1]) - 1 for line in f}  # zero-based

with open(split_file, 'r') as f:
    id_to_split = {int(line.split()[0]): int(line.split()[1]) for line in f}

# Create dicts mapping filename -> label
train_dict = {}
test_dict = {}

for image_id in id_to_path:
    filename = id_to_path[image_id]
    label = id_to_label[image_id]
    if id_to_split[image_id] == 1:
        train_dict[filename] = label
    else:
        test_dict[filename] = label

# Save as JSON
output_base = '/home/praful/scratch/petl/fgvc/CUB_200_2011'
with open(os.path.join(output_base, 'train.json'), 'w') as f:
    json.dump(train_dict, f, indent=2)

with open(os.path.join(output_base, 'test.json'), 'w') as f:
    json.dump(test_dict, f, indent=2)
