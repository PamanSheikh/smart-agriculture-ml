<<<<<<< HEAD
# 🌾 Smart Agriculture Decision Support System

The **Smart Agriculture Decision Support System** is a web-based application developed using **Python and Streamlit**.  
The project is designed to assist **Indian farmers and students** by providing **simple, understandable, and bilingual (English + Hindi)** recommendations related to agriculture.

The system focuses on **clarity, usability, and practical decision-making**, especially for users with limited technical knowledge.

---

## 🎯 Project Objectives

- Recommend suitable crops based on soil and weather conditions
- Suggest appropriate fertilizers based on nutrient levels
- Predict crop yield in a simple and descriptive manner
- Provide an easy-to-use **Farmer Mode** using sliders
- Support **English and Hindi** language throughout the application

---

## 🧩 Major Features

### 🌱 Crop Recommendation
- Suggests the best crop based on:
  - Soil nutrients (N, P, K)
  - Temperature
  - Rainfall
  - Soil pH and humidity
- Displays crop description in **English + Hindi**

---

### 🧪 Fertilizer Recommendation
- Recommends fertilizer based on nutrient deficiency
- Uses **NPK comparison logic**
- Farmer Mode includes **sliders with fixed ranges**
- Explains why a fertilizer is recommended
- Avoids technical agricultural terms where possible

---

### 📈 Yield Prediction
- Predicts expected crop yield
- Inputs include:
  - Crop
  - Season
  - Area
  - Rainfall
- Output is shown in a **descriptive and farmer-friendly format**

---

## 👨‍🌾 Application Modes

### 1️⃣ Farmer Mode
- Slider-based inputs
- Simple language
- Hindi + English labels
- No technical values required from the user

### 2️⃣ Expert Mode
- Numerical inputs
- Intended for students, researchers, and demonstrations

---

## 🌐 Bilingual Support

All major inputs and outputs are shown in:
- **English**
- **Hindi**

Example:
> Crop Recommendation | पिक शिफारस  
> Fertilizer Recommendation | खत शिफारस  

This ensures accessibility for **Indian farmers**.

---

## 🛠️ Technologies Used

- Python
- Streamlit (UI)
- NumPy
- Joblib
- Scikit-learn (optional / model-based logic)

---

## 📂 Project Structure

Smart-Agriculture-ML/
│
├── app.py # Main Streamlit application
├── models/ # Saved ML / rule-based models
├── README.md # Project documentation
└── requirements.txt # Required libraries

---

## ⚙️ How the System Works (Logic)

### 🌱 Crop Recommendation Logic
- Soil type and weather inputs are mapped to nutrient values
- These values are passed to a trained model / rule logic
- The most suitable crop is predicted

---

### 🧪 Fertilizer Recommendation Logic
- The system checks:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
- The nutrient with the **lowest value** is identified
- Fertilizer is recommended accordingly:
  - Low N → Urea
  - Low P → DAP
  - Low K → MOP

This makes the recommendation **logical and explainable**.

---

### 📈 Yield Prediction Logic
- Based on crop, season, rainfall, and area
- Output is simplified for better understanding
- Shown in tons per hectare with explanation

---

## ▶️ How to Run the Project

```bash
streamlit run app.py
=======
# smart-agriculture-ml
Machine learning based decision support system for crop recommendation, fertilizer recommendation and yield prediction.
>>>>>>> 9806ef0c0ef0e8f323dc3c4ccc98653c70a9ab41
