import json
import os
import ollama

brackets = ["<3ms", "3-4ms", "4-5ms", "5-10ms", "10ms-1s", ">1s"]

start_prompt = "You are an expert in predicting the runtime of a piece of Python code. Your task is to predict the runtime of a Python code snippet when executed via Google Colab, using buckets. The Colab Runtime was set up with the following settings: Runtimetype: Python 3 Hardware accelerator: T4 GPU Runtime-version: Newest (reccomended). You must respond with ONLY one of the following bracket labels, nothing else: <3ms, 3-4ms, 4-5ms, 5-10ms, 10ms-1s, >1s. Do not include any explanation, punctuation or extra text, just the bracket label. Make sure to only respond with the bracket label and nothing else. Here is an example of how you should respond: <3ms. Now, please predict the runtime of the following code snippet:"

path = "C:\\Users\\hulsm\\Documents\\Scriptie\\data_and_generation\\combined_final_data\\"

def open_data(file_path):
    print(f"Opening data from {file_path}...")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def predict_runtime(code):
    user_message = f"Here is the code snippet:\n{code}"
    response = ollama.chat(
        model= "gemma4:e2b",
        messages=[
            {"role": "system", "content": start_prompt},
            {"role": "user", "content": user_message}
        ], 
        options={"temperature": 0.1},
        think = False)
    prediction = response['message']['content'].strip()
    if prediction not in brackets:
        print(f"Unexpected prediction: {prediction}")
        if prediction == "<1s":
            return "10ms-1s"
        if prediction == "<10ms":
            return "5-10ms"
        if prediction == "<5ms":
            return "4-5ms"
        if prediction == "<1ms":
            return "3-4ms"
        predict_runtime(code)  # Retry prediction
    return prediction

def main():
    data = open_data(os.path.join(path, "combined_final_data_with_LLM_predictions_gemma4.json"))
    print("Starting predictions...")
    for item in data:
        if item["llm_prediction"] != None:
            continue
        code_snippet = item["code"]
        print(f"Predicting runtime for code snippet:\n{item['id']}\n")
        prediction = predict_runtime(code_snippet)
        print(f"Predicted runtime: {prediction}")
        item["llm_prediction"] = prediction

    with open(os.path.join(path, "combined_final_data_with_LLM_predictions_gemma4.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()