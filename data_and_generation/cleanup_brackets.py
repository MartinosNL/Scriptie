import os
import json

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\final_data\\"

def main():
    file = os.path.join(path, "final_data_with_LLM_predictions.json")
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    cleaned_data = []
    for item in data:
        if item["runtime_bracket"] == '0-3ms':
            item["runtime_bracket"] = '<3ms'
            print(item["runtime_bracket"])
            cleaned_data.append(item)
        else:
            cleaned_data.append(item)

    brackets = set(item["runtime_bracket"] for item in data)
    print(brackets)

    with open(os.path.join(path, "final_data_with_LLM_predictions.json"), "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
    