import json
import os

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def main():
    runtime = open_data(os.path.join(path, "runtimes_parsed_solutions_v1.json"))
    code_data = open_data(os.path.join(path, "data\\parsed_solutions_v1.json"))
    combined_data = []
    for puzzle_id, runtime in runtime:
        code_entry = next((item for item in code_data if item["id"] == puzzle_id), None)
        if code_entry:
            combined_data.append({
                "id": puzzle_id,
                "year": code_entry["year"],
                "day": code_entry["day"],
                "code": code_entry["code"],
                "runtime": runtime
            })
        else:
            print(f"No code entry found for puzzle ID {puzzle_id}")
    
    with open(os.path.join(path, "combined_parsed_solutions_v1.json"), "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2)


if __name__ == "__main__":
    main()