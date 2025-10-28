# 🩺 Diabetes Prediction System (Flask & Random Forest)

A web application built using **Flask** to predict the likelihood of diabetes based on diagnostic measurements. The system utilizes a pre-trained **Random Forest Classifier** model.

## ✨ Features

* **Web Interface:** Simple and intuitive form for inputting 8 patient features.
* **Machine Learning Model:** Uses a **Random Forest Classifier** trained on the Pima Indians Diabetes Dataset.
* **Data Preprocessing:** Implements the **`StandardScaler`** to ensure user input is correctly normalized before prediction.

---

## 📂 Project Structure

This repository follows a standard Flask application structure:

| File/Folder | Description |
| :--- | :--- |
| **`app.py`** | **Main Application Logic.** Handles Flask routing, loads the model/scaler, captures form data, scales the input, and returns the final prediction. |
| **`diabetes_predictor.pkl`** | The trained **Random Forest Classifier** model file. |
| **`scaler.pkl`** | The saved **StandardScaler** object. **Crucial** for transforming user input data correctly. |
| **`requirements.txt`** | A list of all Python libraries (`Flask`, `scikit-learn`, `numpy`, etc.) required for the project. |
| **`templates/`** | **HTML Views.** Contains the web pages served by Flask (`index.html` and `result.html`). |
| **`static/`** | **Assets Folder.** Stores static files used for design, containing the `style.css` stylesheet. |

---

## 🚀 Installation and Setup

Follow these steps to get the application running on your local machine.

### Prerequisites

You must have **Python 3** installed.
