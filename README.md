# Brain Tumor Diagnosis Assistant

## Project Overview

A hybrid system for classifying brain tumors from MRI scans. Combines a CNN model with a meta-learner and rule-based decision engine to improve diagnostic reliability.

## Dataset Source

Kaggle Brain Tumor MRI Dataset: https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

- 4 classes: glioma, meningioma, pituitary, no tumor
- 5712 training images, 1311 test images

## Model Architecture

- Base model: Xception (pretrained on ImageNet)
- Meta-learner: Logistic Regression combining CNN outputs with shape features (area, perimeter, circularity, solidity, irregularity)
- Rule engine: Uses confidence threshold (0.80) and irregularity threshold to flag uncertain cases for specialist review

## Instructions to Reproduce Results

1. Download the dataset from Kaggle
2. Install requirements:
   ```
   pip install tensorflow numpy pandas matplotlib seaborn scikit-learn pillow scikit-image
   ```
3. Open `brain_tumor.ipynb` and update the dataset paths to match your local setup
4. Run all cells in the notebook
