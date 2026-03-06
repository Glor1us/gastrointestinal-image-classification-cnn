# gastrointestinal-image-classification-cnn
Deep learning project for gastrointestinal image classification using CNN architectures and the Kvasir dataset.
Gastrointestinal Image Classification using Deep Learning
Project Overview

This project explores deep learning approaches for automatic classification of gastrointestinal endoscopic images using convolutional neural networks (CNNs).

The goal is to evaluate how different neural network architectures perform on medical image classification tasks.

The models were trained and evaluated using the Kvasir dataset, a widely used dataset for gastrointestinal disease analysis.

Dataset

This project uses the Kvasir Dataset, which contains labeled endoscopic images representing various gastrointestinal conditions.

Dataset source:

https://datasets.simula.no/kvasir/

The images were resized and preprocessed before training.

Models Used

The following deep learning architectures were evaluated:

InceptionV3

MobileNetV3

DenseNet121

EfficientNetB0

All models were trained using transfer learning.

Methodology

Image preprocessing and resizing

Train / validation / test split

Transfer learning using pretrained CNN models

Fine-tuning of model layers

Evaluation using classification metrics

Evaluation Metrics

Model performance was evaluated using:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

Results

The models achieved different performance levels depending on architecture complexity and feature extraction capability.

Example results include:

Accuracy comparison between architectures

Confusion matrices

Training curves

Example visualization:

Accuracy comparison between CNN architectures

(Insert plots in the results folder)

Project Structure
dataset_info/        Dataset description
notebooks/           Training notebooks
results/             Graphs and evaluation outputs
models/              Model information
requirements.txt     Python dependencies
Technologies Used

Python

PyTorch

OpenCV

Scikit-learn

Matplotlib

Author

Vladislav Skobelev

Computer Engineering Student
