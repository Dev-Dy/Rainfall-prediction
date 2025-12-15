````markdown
# 🌧️ Rainfall Prediction System

A **production-ready machine learning application** built using **Python** to predict rainfall based on historical weather data sourced from **Kaggle**. The project follows **industry best practices** such as environment-based configuration, modular code design, automated dataset handling, and an interactive **Streamlit web interface**.

---

## 📌 Overview

Accurate rainfall prediction plays a critical role in agriculture, water resource management, and disaster preparedness. This project applies **machine learning techniques** to analyze historical rainfall data and generate predictions in a reproducible and scalable manner.

---

## 🚀 Key Features

- Machine learning–based rainfall prediction  
- Automated dataset download using Kaggle API  
- Secure configuration through environment variables  
- End-to-end ML pipeline (data preprocessing → training → evaluation)  
- Interactive web interface built with Streamlit  
- Production-ready, ATS- and interview-friendly implementation  

---

## 🛠️ Technology Stack

- **Python**
- **Pandas, NumPy** – Data processing
- **scikit-learn** – Machine learning
- **Kaggle API** – Dataset integration
- **Streamlit** – Web application
- **python-dotenv** – Environment management

---

## 📊 Dataset

- Source: **Kaggle**
- Contains historical rainfall data used for training and evaluation
- Dataset is automatically downloaded and cached locally during runtime

---

## 🔐 Environment Configuration

1. Create an environment file:
   ```bash
   cp .env.example .env
````

2. Add your Kaggle credentials to `.env`:

   ```env
   KAGGLE_USERNAME=your_kaggle_username
   KAGGLE_KEY=your_kaggle_api_key
   KAGGLE_DATASET=dataset-owner/dataset-name
   ```

> ⚠️ Do not commit `.env` files or Kaggle credentials to version control.

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/Dev-Dy/Rainfall-prediction
cd Rainfall-prediction
```

### Step 2: Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the machine learning pipeline

```bash
python main.py
```

This will:

* Download the dataset from Kaggle (if not already present)
* Preprocess the data
* Train the machine learning model
* Display evaluation metrics

### Step 5: Run the Streamlit web application

```bash
streamlit run streamlit_app.py
---

## 🧠 Machine Learning Workflow

* Dataset retrieval from Kaggle
* Data cleaning and preprocessing
* Feature encoding
* Model training using Random Forest
* Model evaluation with standard metrics
* Real-time prediction through Streamlit UI

---

## 📜 License

This project is open-source and intended for educational and demonstration purposes.

```