import ast
import os
import json

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\used_data\\"

def main():
    input_file = os.path.join(path, "clean_combined\\clean_combined.json")
    output_file = os.path.join(path, "ast_combined\\clean_combined_ast.json")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        code = item["code"]
        try:
            item["ast"] = ast.dump(ast.parse(code))
        except Exception as e:
            print(f"Error parsing code: {e}")
            item["ast"] = None
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    


if __name__ == "__main__":
    main()