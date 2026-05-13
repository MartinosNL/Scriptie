import json
import os
import re

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def parse_data(data):
    print("Parsing data...")
    pattern = r"open\(['\"]?[\w.]+['\"]?"
    replace_pattern = r"open('input.txt'"

    parsed_data = []

    for item in data:
        if "open(" in item["code"]:
            print(f"Found open() in year {item['year']} day {item['day']}")
            item["code"] = re.sub(pattern, replace_pattern, item["code"])
            parsed_data.append(item)
            print(f"Updated code for year {item['year']} day {item['day']}")
        else:
            print(f"No open() found in year {item['year']} day {item['day']}")

    with open(os.path.join(path, f"runnable_data\\parsed_solutions_p1.json"), "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=2)

def main():
    data = open_data(os.path.join(path, "filtered_solutions_p1.json"))
    parse_data(data)

if __name__ == "__main__":
    main()