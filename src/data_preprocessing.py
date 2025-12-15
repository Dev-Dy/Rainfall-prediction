import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from dotenv import load_dotenv
from src.kaggle_loader import download_kaggle_dataset


def load_and_preprocess_data():
    load_dotenv()
    download_kaggle_dataset()

    data_dir = os.getenv("DATA_DIR", "data")

    csv_file = next(
        f for f in os.listdir(data_dir) if f.endswith(".csv")
    )

    df = pd.read_csv(os.path.join(data_dir, csv_file))

    df.drop_duplicates(inplace=True)
    df.fillna(method="ffill", inplace=True)

    encoder = LabelEncoder()
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = encoder.fit_transform(df[col])

    target = "Rainfall"

    X = df.drop(columns=[target])
    y = df[target]

    return train_test_split(X, y, test_size=0.2, random_state=42)
