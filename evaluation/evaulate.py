from sklearn import metrics
import json
import os

file_path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"

def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


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


def main():
    data = get_data(os.path.join(file_path, "combined_final_data_with_majority_baseline.json"))
    y_true = [item["runtime_bracket"] for item in data]
    y_pred = [item["majority_baseline_prediction"] for item in data]
    mae = mean_absolute_error(y_true, y_pred)
    print(f"Mean Absolute Error: {mae}")

    print(metrics.confusion_matrix(y_true, y_pred, labels=['<3ms', '3-4ms', '4-5ms', '5-10ms', '10ms-1s', '>1s']))
    print(metrics.classification_report(y_true, y_pred))

if __name__ == "__main__":
    main()