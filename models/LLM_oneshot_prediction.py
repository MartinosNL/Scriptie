import json
import os
import ollama

brackets = ["<3ms", "3-5ms", "5-10ms", "10ms-1s", ">1s"]

start_prompt = "You are an expert in predicting the runtime of a piece of Pyhton code. Your task is to predict the runtime of a Python code snippet when executed via Google Colab. You must respond with ONLY one of the following bracket labels, nothing else: <3ms, 3-5ms, 5-10ms, 10ms-1s, >1s. Do not include any explanation, punctuation or extra text, just the bracket label."

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\final_data\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def predict_runtime(code):
    user_message = f"Here is the code snippet:\n{code}"
    response = ollama.chat(
        model= "llama3.1:8b",
        messages=[
            {"role": "system", "content": start_prompt},
            {"role": "user", "content": user_message}
        ], 
        options={"temperature": 0.0})
    prediction = response['message']['content'].strip()
    if prediction not in brackets:
        print(f"Unexpected prediction: {prediction}")
        return None
    return prediction

def main():
    data = open_data(os.path.join(path, "final_data_v1.json"))
    for item in data:
        code_snippet = item["code"]
        prediction = predict_runtime(code_snippet)
        print(f"Predicted runtime: {prediction}")
        item["llm_prediction"] = prediction

    with open(os.path.join(path, "final_data_with_predictions_v1.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()