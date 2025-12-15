from src.data_preprocessing import load_and_preprocess_data
from src.train_model import train_model
from src.evaluate import evaluate_model


def main():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    model = train_model(X_train, y_train)

    accuracy, report, matrix = evaluate_model(
        model, X_test, y_test
    )

    print(f"Accuracy: {accuracy:.4f}")
    print(report)
    print(matrix)


if __name__ == "__main__":
    main()
