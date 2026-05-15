from sklearn import metrics
import json
import os

file_path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\final_data\\"

def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def main():
    data = get_data(os.path.join(file_path, "final_data_with_LLM_predictions_v1.json"))
    data += get_data(os.path.join(file_path, "final_data_with_LLM_predictions.json"))
    y_true = [item["runtime_bracket"] for item in data]
    y_pred = [item["llm_prediction"] for item in data]

    print(y_true)
    print('-'*50)
    print(y_pred)
    print(metrics.confusion_matrix(y_true, y_pred, labels=['<3ms', '3-4ms', '4-5ms', '5-10ms', '10ms-1s', '>1s']))

    print(metrics.classification_report(y_true, y_pred))

if __name__ == "__main__":
    main()