# using the model locally ----------> success 
# from flask import Flask , request, jsonify
# from transformers import pipeline

# app = Flask(__name__)
# # Load question-answering pipeline
# qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.json
#     question = data.get("question")
#     context = data.get("context")

#     if not question or not context:
#         return jsonify({"error": "Missing question or context"}), 400

#     result = qa_pipeline(question= question, context= context)
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)

# using api ----------> success
from flask import Flask, request, jsonify
import requests

# Define the API URL and the model
url = "https://router.huggingface.co/hf-inference/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}

# Define your payload with question and context

app = Flask(__name__)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()  # Correct method to get JSON data
    question = data.get("question")
    context = data.get("context")
    payload = {"inputs": {"question": f"{question}", "context": f"{context}"}}

    


# Send the request
    response = requests.post(url, headers=headers, json=payload)

# Get the result from the API
    result = response.json()


    print(result)
    return result

if __name__ == '__main__':
    app.run(debug=True)
