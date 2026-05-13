from radon.complexity import cc_visit, cc_rank
import os
import json

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\used_data\\"

def calculate_complexity(code):
    blocks = cc_visit(code)
    average = sum(b.complexity for b in blocks) / len(blocks) if blocks else 0
    return round(average, 2), cc_rank(average)

def main():
    input_file = os.path.join(path, "ast_combined\\clean_combined_v1_ast.json")
    output_file = os.path.join(path, "complexity_ast_combined\\combined_ast_complexity_v1.json")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        code = item["code"]
        try:
            complexity, rank = calculate_complexity(code)
            item["complexity"] = complexity
            item["complexity_rank"] = rank
        except Exception as e:
            print(f"Error analyzing code: {e}")
            item["complexity"] = None
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    


if __name__ == "__main__":
    main()