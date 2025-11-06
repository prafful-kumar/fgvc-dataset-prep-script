# FGVC Dataset Preprocessing Scripts

This repository contains a collection of Python scripts to preprocess popular Fine-Grained Visual Categorization (FGVC) datasets.

The primary goal of these scripts is to convert the original, often complex, annotation formats (like MATLAB `.mat` files or multiple `.txt` files) into simple, standardized `train.json` and `test.json` files. This JSON format provides a clean, easy-to-parse mapping between image filenames and their corresponding class labels, which is ideal for building custom data loaders in deep learning frameworks.

## Supported Datasets

* **CUB-200-2011:** (`cub_200_json.py`)
* **Stanford Dogs:** (`dogs_fgvc.py`)
* **Stanford Cars:** (`cars_fgvc.py`)
* **NABirds:** (`nabirds_fgvc.py`)
* **Oxford 102 Flowers:** (`flowers_fgvc.py`)

---

## How to Use

### 1. Prerequisites

* Python 3
* The `scipy` library (for scripts that read `.mat` files)

You can install the main dependency using pip:
```bash
pip install scipy

```


FGVC comprises 5 fine-grained visual classification dataset. The datasets can be downloaded following the official links. We split the training data if the public validation set is not available. The splitted dataset can be found here: [Download Link](https://huggingface.co/datasets/XiN0919/FGVC/resolve/main/json.zip?download=true).
  
- [CUB200 2011](https://data.caltech.edu/records/65de6-vp158)
- [NABirds](http://info.allaboutbirds.org/nabirds/)
- [Oxford Flowers](https://www.robots.ox.ac.uk/~vgg/data/flowers/)
- [Stanford Dogs](http://vision.stanford.edu/aditya86/ImageNetDogs/main.html)
- [Stanford Cars](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)
