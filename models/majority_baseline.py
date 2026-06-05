import os
import json


def main():
    filepath = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"
    with open(os.path.join(filepath, "combined_final_data.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    bracket_counts = {}
    for item in data:
        bracket = item["runtime_bracket"]
        if bracket in bracket_counts:
            bracket_counts[bracket] += 1
        else:
            bracket_counts[bracket] = 1
    majority_class = max(bracket_counts, key=bracket_counts.get)
    for item in data:
        item["majority_baseline_prediction"] = majority_class
    with open(os.path.join(filepath, "combined_final_data_with_majority_baseline.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)




if __name__ == "__main__":
    main()