import os
import json
from scipy.io import loadmat

root_dir = '/home/praful/scratch/petl/fgvc/OxfordFlower'
img_dir = 'jpg'
labels = loadmat(os.path.join(root_dir, 'imagelabels.mat'))['labels'][0]
splits = loadmat(os.path.join(root_dir, 'setid.mat'))

train_ids = splits['trnid'][0]
val_ids = splits['valid'][0]
test_ids = splits['tstid'][0]

def make_json(image_ids, labels):
    return {f'image_{i:05d}.jpg': int(labels[i-1]) - 1 for i in image_ids}

train_dict = make_json(train_ids, labels)
val_dict = make_json(val_ids, labels)
test_dict = make_json(test_ids, labels)

with open(os.path.join(root_dir, 'train.json'), 'w') as f:
    json.dump(train_dict, f, indent=2)
with open(os.path.join(root_dir, 'val.json'), 'w') as f:
    json.dump(val_dict, f, indent=2)
with open(os.path.join(root_dir, 'test.json'), 'w') as f:
    json.dump(test_dict, f, indent=2)
