```markdown
# 🌧️ Rainfall Prediction System

A production-ready **machine learning project in Python** that predicts rainfall using historical weather data sourced from **Kaggle**. The project follows industry best practices such as modular code structure, environment-based configuration, automated dataset download, and an interactive **Streamlit** web interface.

---

## 🚀 Features

- Rainfall prediction using machine learning
- Automated dataset download from Kaggle using API
- Secure environment variable management
- Modular and scalable codebase
- Interactive web application using Streamlit
- Reproducible and interview-ready setup

---

## 🏗️ Project Structure

```

Rainfall-prediction/
│
├── data/                     # Kaggle dataset (auto-downloaded)
│
├── src/
│   ├── **init**.py
│   ├── kaggle_loader.py      # Kaggle dataset download & caching
│   ├── data_preprocessing.py # Data cleaning and preprocessing
│   ├── train_model.py        # Model training
│   ├── evaluate.py           # Model evaluation
│
├── streamlit_app.py          # Streamlit web interface
├── main.py                   # Command-line entry point
├── requirements.txt          # Project dependencies
├── .env.example              # Environment variables template
├── .gitignore
└── README.md

````

---

## 📊 Dataset

- Source: **Kaggle**
- Historical rainfall data used for prediction
- Automatically downloaded and cached locally on first run

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- scikit-learn
- Kaggle API
- Streamlit
- python-dotenv

---

## 🔐 Environment Setup

1. Copy the environment template:
   ```bash
   cp .env.example .env
````

2. Update `.env` with your Kaggle credentials:

   ```env
   KAGGLE_USERNAME=your_kaggle_username
   KAGGLE_KEY=your_kaggle_api_key
   KAGGLE_DATASET=dataset-owner/dataset-name
   ```

⚠️ Do not commit `.env` or Kaggle credentials.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dev-Dy/Rainfall-prediction
cd Rainfall-prediction
```

### 2️⃣ Create and activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the ML pipeline

```bash
python main.py
```

### 5️⃣ Run the Streamlit app

```bash
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 Model Workflow

1. Download dataset from Kaggle
2. Preprocess and clean data
3. Encode features
4. Train machine learning model
5. Evaluate performance
6. Predict rainfall via Streamlit UI

---

## 📜 License

This project is open-source and intended for educational and demonstration purposes.

```
```
