from radon.complexity import cc_visit, cc_rank, cc_visit
import os
import json

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"

def calculate_complexity(code):
    blocks = cc_visit(code)
    average = sum(b.complexity for b in blocks) / len(blocks) if blocks else 0
    return round(average, 2), cc_rank(average)

def main():
    input_file = os.path.join(path, "combined_final_data.json")
    output_file = os.path.join(path, "combined_final_data.json")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        if item["complexity"] is not None:
            continue
        code = item["code"]
        try:
            complexity, rank = calculate_complexity(code)
            item["complexity"] = complexity
            item["complexity_rank"] = rank
        except Exception as e:
            print(f"Error analyzing code:{item['id']} {e.lineno} {e.msg}")
            item["complexity"] = None
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    


if __name__ == "__main__":
    main()