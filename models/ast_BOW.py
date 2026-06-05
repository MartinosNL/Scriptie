import json
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import scipy.sparse as sp
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt


path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"


def mean_absolute_error(y_true, y_pred):
    bracket_values = {
        "<3ms": 1,
        "3-4ms": 2,
        "4-5ms": 3,
        "5-10ms": 4,
        "10ms-1s": 5,
        ">1s": 6
    }
    
    total_error = 0
    for true, pred in zip(y_true, y_pred):
        if pred is None:
            continue  # Skip if prediction is None
        if true is None:
            continue  # Skip if true value is None
        true_value = bracket_values[true]
        pred_value = bracket_values[pred]
        total_error += abs(true_value - pred_value)
    
    return total_error / len(y_true)


def get_data(filename):
    input_file = os.path.join(path, filename)
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def preprocess_data(df):
     # Target variable
    le = LabelEncoder()
    y = le.fit_transform(df["runtime_bracket"])

    # TF-IDF features
    vectorizer = TfidfVectorizer(max_features=1000)
    x = vectorizer.fit_transform(df["ast"])

    return x, y, le


def train_model(x, y, le):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    all_y_true = []
    all_y_pred = []

    for fold, (train_idx, test_idx) in enumerate(kf.split(x), 1):
        X_train, X_test = x[train_idx], x[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Decode labels back to bracket strings
        y_test_labels = le.inverse_transform(y_test)
        y_pred_labels = le.inverse_transform(y_pred)

        all_y_true.extend(y_test_labels)
        all_y_pred.extend(y_pred_labels)

    print(classification_report(all_y_true, all_y_pred))
    print(f"MAE: {mean_absolute_error(all_y_true, all_y_pred):.3f}")
    print(confusion_matrix(all_y_true, all_y_pred, labels=['<3ms', '3-4ms', '4-5ms', '5-10ms', '10ms-1s', '>1s']))
    return all_y_pred



def main():
    data = get_data("combined_final_data.json")
    df = pd.DataFrame(data)

    x, y, le = preprocess_data(df)

    all_y_pred = train_model(x, y, le)

    combined_results = []
    for item, pred in zip(data, all_y_pred):
        item["ast_BOW_prediction"] = pred
        combined_results.append(item)

    with open(os.path.join(path, "ast_BOW_predictions.json"), "w", encoding="utf-8") as f:
        json.dump(combined_results, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()