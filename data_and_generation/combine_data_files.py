import json
import os


def get_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    file_path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\final_data\\"
    id = 1
    data1 = get_data(os.path.join(file_path, "final_data_v1.json"))
    for item in data1:
        item["id"] = id
        id += 1
    print(f"Last ID in data1: {data1[-1]['id']}")
    data2 = get_data(os.path.join(file_path, "final_data.json"))
    for item in data2:
        item["id"] = id
        id += 1
    print(f"First ID in data2: {data2[0]['id']}")
    combined_data = data1 + data2

    with open(os.path.join(file_path, "combined_final_data.json"), "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()