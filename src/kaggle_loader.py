import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv


def download_kaggle_dataset():
    load_dotenv()

    dataset = os.getenv("KAGGLE_DATASET")
    data_dir = os.getenv("DATA_DIR", "data")

    os.makedirs(data_dir, exist_ok=True)

    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]
    if csv_files:
        return  # Already downloaded

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset,
        path=data_dir,
        unzip=True
    )
