import streamlit as st
import pandas as pd
from src.data_preprocessing import load_and_preprocess_data
from src.train_model import train_model


DATA_PATH = "data/rainfall.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


@st.cache_resource
def train_cached_model():
    X_train, _, y_train, _ = load_and_preprocess_data(DATA_PATH)
    model = train_model(X_train, y_train)
    return model, X_train.columns


def main():
    st.set_page_config(
        page_title="Rainfall Prediction",
        page_icon="🌧️",
        layout="centered"
    )

    st.title("🌧️ Rainfall Prediction System")
    st.write(
        "Predict rainfall using a machine learning model trained on historical weather data."
    )

    model, feature_columns = train_cached_model()

    st.subheader("Enter Weather Parameters")

    user_input = {}
    for feature in feature_columns:
        user_input[feature] = st.number_input(
            label=feature,
            value=0.0
        )

    input_df = pd.DataFrame([user_input])

    if st.button("Predict Rainfall"):
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("🌧️ Rainfall Expected")
        else:
            st.info("☀️ No Rainfall Expected")


if __name__ == "__main__":
    main()
