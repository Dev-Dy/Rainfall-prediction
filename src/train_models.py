from sklearn.ensemble import RandomForestClassifier


def train_model(X_train, y_train):
    """
    Trains RandomForest model on rainfall data.
    """
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    return model
