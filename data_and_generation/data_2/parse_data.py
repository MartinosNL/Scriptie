import json
import os

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_2\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    
    data = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                data.append(json.loads(line))
    
    return data

def save_data(data):
    filtered = [
         {
            "id": i,
            "year": item["year"],
            "day": item["day"],
            "code": item[f"code"]
         }
         for i, item in enumerate(data, start=1)
    ]
    with open(os.path.join(path, f"filtered_solutions.json"), "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=2)


def main():
    data = open_data(os.path.join(path, "extracted_solutions.jsonl"))
    save_data(data)

    

if __name__ == "__main__":
    main()