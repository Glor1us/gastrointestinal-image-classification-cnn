# Gastrointestinal Image Classification using Deep Learning

Deep learning project for **medical image classification** using CNN architectures on the **Kvasir gastrointestinal dataset**.

This project compares multiple convolutional neural network architectures and evaluates their performance on endoscopic image classification.

---

# Project Overview

Medical image classification is an important task in computer vision and healthcare. Automated analysis of gastrointestinal images can assist doctors in detecting abnormalities and improving diagnostic efficiency.

In this project, several **deep learning CNN architectures** were trained using transfer learning to classify gastrointestinal images.

The models were evaluated and compared using multiple performance metrics.

---

# Google Colab (Run the Project)

To reproduce the experiment easily, open the project in Google Colab:

👉 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1RNxaAZeAhuGJUIs2w6lfMrkqZhnioHy6?usp=sharing

Colab contains the full pipeline:

- dataset loading
- preprocessing
- model training
- evaluation
- visualization of results

This allows anyone to reproduce the results without local setup.

---

# Project Structure

```
Gastrointestinal-Image-Classification-CNN
│
├── notebooks
│   └── training_model.ipynb
│
├── results
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── confusion_matrix.png
│
├── models
│   └── cnn_model.h5
│
├── requirements.txt
│
└── README.md
```

Explanation:

- **notebooks/** — Jupyter notebooks used for training and experiments  
- **results/** — training results and evaluation plots  
- **models/** — saved trained models  
- **requirements.txt** — required Python libraries 

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

# Model Architecture

The project uses Convolutional Neural Networks (CNN) for image classification.

Typical CNN components used:

- Convolution layers
- MaxPooling layers
- Fully connected layers
- Softmax output layer

The model was trained using TensorFlow / Keras.

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

# DenseNet121

<img width="800" height="600" alt="densenet_cm" src="https://github.com/user-attachments/assets/dfe39a51-c6d3-4410-bbab-a11cc71233b0" />

# EfficientNetB0

<img width="800" height="600" alt="efficientnet_cm" src="https://github.com/user-attachments/assets/ea29c4ab-6512-4e64-89b2-27bf8cc65d31" />

# InceptionV3

<img width="900" height="700" alt="inception_cm" src="https://github.com/user-attachments/assets/a25cc2cd-5fa2-484d-ab4f-85038ed06014" />

# MobileNetV3

<img width="800" height="600" alt="mobilenet_cm" src="https://github.com/user-attachments/assets/f4f6cdb2-ea73-42f5-8032-f77a31ba6c49" />


## Training Curve

# DenseNet121

<img width="1200" height="400" alt="densenet_loss" src="https://github.com/user-attachments/assets/447d388e-4e99-4176-9c04-9befd5ce453e" />

# EfficientNetB0

<img width="1200" height="400" alt="efficientnet_loss" src="https://github.com/user-attachments/assets/a60aacba-76f0-4a45-9058-3b25167c8632" />

# InceptionV3

<img width="1200" height="400" alt="inception_loss" src="https://github.com/user-attachments/assets/9ac23aad-42f9-47dc-bd5b-c5b52fc95340" />

# MobileNetV3

<img width="1200" height="400" alt="mobilenet_loss" src="https://github.com/user-attachments/assets/d4eef859-d6ce-4128-be7b-01d81bd6461a" />

---

# Technologies Used

- Python
- PyTorch
- OpenCV
- Scikit-learn
- Matplotlib
- NumPy

---

# How to Run Locally

Clone the repository:

```bash
git clone https://github.com/Glor1us/gastrointestinal-image-classification-cnn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run training:

```bash
python train.py
```

Alternatively, run the project directly in Google Colab.

---

# Author

Vladislav Skobelev

Computer Engineering Student



