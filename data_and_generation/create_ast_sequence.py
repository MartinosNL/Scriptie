import json
import os
import ast


path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"


def main():
    input_file = os.path.join(path, "combined_final_data.json")
    output_file = os.path.join(path, "combined_final_data.json")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        code = item["code"]
        try:
            tree = ast.parse(code)
            nodes = []
            def visit(node):
                nodes.append(type(node).__name__)
                for child in ast.iter_child_nodes(node):
                    visit(child)
            visit(tree)
            item["ast_seq"] = " ".join(nodes)
        except Exception as e:
            print(f"Error parsing code: {item['id']}: {e}")
            item["ast"] = None        


    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()