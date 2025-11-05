# Skin Cancer Detection using Deep Learning (CNN + PyQt5 + REST API)

This project is a complete end-to-end skin cancer detection system built using Deep Learning (TensorFlow/Keras). It includes:

* A Convolutional Neural Network (CNN) model trained to classify benign vs malignant skin lesions.
* A modern PyQt5 desktop application with drag-and-drop image support, asynchronous model loading, and real-time predictions.
* A lightweight backend API server (socket-based REST service) for web or remote usage.
* Future plans for a web client frontend to make predictions directly from browsers.

---

## Table of Contents

1. Project Overview
2. Features
3. System Architecture
4. Model Training
5. Desktop Application (PyQt5)
6. Backend API Server
7. Folder Structure
8. Installation & Setup
9. Usage
10. Future Improvements
11. Tech Stack
12. License

---

## Project Overview

Skin cancer, particularly melanoma, can be deadly if not detected early. This project aims to assist dermatologists and individuals in early identification of potentially malignant skin lesions using AI.

A Convolutional Neural Network (CNN) is trained on labeled images of benign and malignant skin conditions.
The trained model powers both a desktop application and a REST API for serving predictions.

---

## Features

**Deep Learning Model (CNN):**

* 3 convolutional layers with dropout regularization for better generalization.
* Trained on augmented image data for robustness.
* Saves and loads model weights for reuse.

**Desktop GUI (PyQt5):**

* Modern interface with custom stylesheet (`styles.css`).
* Drag & drop and file selection supported.
* Multithreaded model loading for smooth performance.
* Displays prediction probability, result (Benign/Malignant), and severity description.

**REST API Server:**

* Socket-based lightweight backend (no Flask/Django required).
* Accepts `multipart/form-data` image uploads.
* Returns JSON with probability and diagnostic message.
* Designed for integration with web or mobile clients.

**Model Evaluation:**

* Accuracy and loss visualization.
* Confusion matrix and classification report.
* Test image previews with predictions.

---

## System Architecture

Dataset → CNN Model Training → Saved Model (H5)
     ↙              ↘
   PyQt5 Desktop App      REST API Server
            ↘      ↙
       Future Web Client (Frontend)

---

## Model Training

The training pipeline includes:

* ImageDataGenerator for real-time data augmentation (rotation, zoom, flip, etc.).
* CNN architecture:

  * Conv2D + MaxPooling2D layers (32, 64, 128 filters)
  * Dense(512) + Dropout(0.5)
  * Output: Dense(1, activation='sigmoid')
* Compiled using Adam optimizer and binary cross-entropy loss.
* Includes EarlyStopping and ReduceLROnPlateau callbacks.

Models are saved as:

* `skin_cancer_cnn.h5` (HDF5 format)
* `saved_model/` (TensorFlow SavedModel format)

Includes performance metrics:

* Training vs validation accuracy plots.
* Confusion matrix visualization.

---

## Desktop Application (PyQt5)

A user-friendly GUI built with PyQt5 that allows easy prediction of skin cancer probability:

* Loads model asynchronously using QThread to prevent freezing.
* Drag-and-drop image support.
* Image preview with automatic scaling.
* Displays real-time predictions and severity levels.

**Severity Scale Example:**

| Probability | Interpretation       |
| ----------- | -------------------- |
| ≤ 0.5       | Benign / No concern  |
| ≤ 0.6       | Mild irregularity    |
| ≤ 0.7       | Moderate abnormality |
| ≤ 0.8       | Malignant potential  |
| ≤ 0.9       | High-risk melanoma   |
| > 0.95      | Critical melanoma    |

---

## Backend API Server

A simple REST-like backend built using sockets and multithreading.
It allows remote clients to make predictions using the trained CNN model.

**Endpoints:**

| Method | Path       | Description                                     |
| ------ | ---------- | ----------------------------------------------- |
| GET    | `/`        | Returns API information                         |
| POST   | `/predict` | Accepts an image and returns prediction results |

**Sample Response:**

```json
{
  "probability": "0.84",
  "description": "High-risk melanoma features observed."
}
```

**Server URL:**

```
http://127.0.0.1:9889
```

This server can be integrated with a web frontend or mobile application for remote use.

---

## Usage

**Using the PyQt5 App**

* Launch the GUI.
* Wait for "Model loaded!" message.
* Drag & drop an image or click “Select Image”.
* View prediction, probability, and severity description.

**Using the REST API**
Send a POST request to `/predict` with an image using `curl` or `Postman`.

Example:

```
POST /predict
Content-Type: multipart/form-data
```

---

## Future Improvements

* Develop a web-based frontend (React/Next.js).
* Add Grad-CAM visualization for explainability.
* Replace socket server with Flask/FastAPI for better API support.
* Enable cloud deployment (AWS/GCP).
* Add automatic updates for PyQt5 application.
* Extend to Android/iOS platforms.

---

## Tech Stack

* **Machine Learning:** TensorFlow, Keras, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn
* **Frontend (Desktop):** PyQt5
* **Backend (API):** Python Socket Server
* **Environment:** Python 3.8+
* **Planned Frontend:** React / HTML5 / CSS3

---

## License

This project is released under the MIT License. You are free to use, modify, and distribute it with proper attribution.

---

## Author

**Chinmay Krishn Roy**
Software Developer
GitHub: [[https://github.com/](https://github.com/chinmaykrishnroy)chinmaykrishnroy]
LinkedIn: [[https://linkedin.com/in/](https://linkedin.com/in/chinmaykrishnroy)chinmaykrishnroy]

*"Early detection saves lives — let AI help detect skin cancer before it's too late."*
