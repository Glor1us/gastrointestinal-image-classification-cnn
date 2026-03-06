# Gastrointestinal Image Classification using Deep Learning

Deep learning project for **medical image classification** using CNN architectures on the **Kvasir gastrointestinal dataset**.

This project compares multiple convolutional neural network architectures and evaluates their performance on endoscopic image classification.

---

# Project Overview

Medical image classification is an important task in computer vision and healthcare. Automated analysis of gastrointestinal images can assist doctors in detecting abnormalities and improving diagnostic efficiency.

In this project, several **deep learning CNN architectures** were trained using transfer learning to classify gastrointestinal images.

The models were evaluated and compared using multiple performance metrics.

---

# Dataset

This project uses the **Kvasir Dataset**, which contains labeled endoscopic images representing different gastrointestinal conditions.

Dataset source:

https://datasets.simula.no/kvasir/

The dataset contains images from multiple classes of gastrointestinal findings.

Images were preprocessed before training.

Preprocessing steps:

- Image resizing
- Normalization
- Train / validation / test split
- Data augmentation

---

# Models Used

The following deep learning architectures were evaluated:

- InceptionV3
- MobileNetV3
- DenseNet121
- EfficientNetB0

All models were trained using **transfer learning with pretrained weights**.

---

# Methodology

The training pipeline consisted of the following steps:

1. Dataset preprocessing
2. Image resizing to a fixed resolution
3. Dataset splitting (train / validation / test)
4. Transfer learning using pretrained CNN models
5. Model training and fine-tuning
6. Performance evaluation

---

# Evaluation Metrics

Model performance was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

# Results

Below are example visualizations from the experiments.

## Model Accuracy Comparison

<img width="700" height="500" alt="comparison_accuracy" src="https://github.com/user-attachments/assets/3b091e29-1935-446f-a71a-149926e78bcb" />


## Confusion Matrix

#DenseNet

<img width="800" height="600" alt="densenet_cm" src="https://github.com/user-attachments/assets/dfe39a51-c6d3-4410-bbab-a11cc71233b0" />

## Training Curve

<img width="1200" height="400" alt="densenet_loss" src="https://github.com/user-attachments/assets/447d388e-4e99-4176-9c04-9befd5ce453e" />


---

# Technologies Used

- Python
- PyTorch
- OpenCV
- Scikit-learn
- Matplotlib
- NumPy

---

# Installation

Clone the repository:


#Author

Vladislav Skobelev

Computer Engineering Student



