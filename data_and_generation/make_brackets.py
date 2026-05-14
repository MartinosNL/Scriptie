import os
import json

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\"

def calculate_brackets(runtime):
    if isinstance(runtime, str) and runtime == "Timeout":
        return ">1s"
    else:
        if runtime < 0.003:
            return "<3ms"
        elif runtime < 0.004:
            return "3-4ms"
        elif runtime < 0.005:
            return "4-5ms"
        elif runtime < 0.01:
            return "5-10ms"
        elif runtime < 1:
            return "10ms-1s"
        else:
            return ">1s"
    


def main():
    input_file = os.path.join(path, "used_data\\complexity_ast_combined\\combined_ast_complexity_v1.json")
    output_file = os.path.join(path, "final_data\\final_data_v1.json")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        runtime = item["runtime"]
        item["runtime_bracket"] = calculate_brackets(runtime)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    


if __name__ == "__main__":
    main()