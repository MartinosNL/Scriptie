import os
import json
import pandas as pd

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\used_data\\clean_combined\\"

def main():
    input_file = os.path.join(path, "clean_combined_v1.json")
    output_file = os.path.join(path, "clean_combined_v1.xlsx")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")
        


if __name__ == "__main__":
    main()