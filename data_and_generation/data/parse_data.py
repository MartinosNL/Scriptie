import json
import os

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_data(data, part):
    print(f"Saving filtered data for part {part}...")
    filtered = [
         {
            "id": i,
            "year": item["year"],
            "day": item["day"],
            "code": item[f"part{part}"]
         }
         for i, item in enumerate(data, start=1)
    ]
    with open(os.path.join(path, f"filtered_solutions_p{part}.json"), "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=2)


def main():
    data = open_data(os.path.join(path, "raw_solutions.json"))
    save_data(data, 1)
    save_data(data, 2)

    

if __name__ == "__main__":
    main()