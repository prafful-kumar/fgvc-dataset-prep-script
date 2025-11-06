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

Example: In cub_200_json.py, you must change this line:

# Before
root_dir = '/home/praful/scratch/petl/fgvc/CUB_200_2011'

# After (example)
root_dir = '/my/local/path/to/CUB_200_2011'
