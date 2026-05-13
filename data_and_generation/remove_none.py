import json
import os

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\used_data\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    data = open_data(os.path.join(path, "combined_solutions\\combined_parsed_solutions.json"))

    cleaned_data = []

    for item in data:
        if not item["runtime"]:
            print(f"Removing item with id {item['id']} because runtime is None")
        else:
            cleaned_data.append(item)
    with open(os.path.join(path, "clean_combined\\clean_combined.json"), "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2)

if __name__ == "__main__":
    main()