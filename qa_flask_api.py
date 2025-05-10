from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Use your environment variable or directly paste the key
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    context = data.get("context")

    if not question or not context:
        return jsonify({"error": "Missing question or context"}), 400

    payload = {"inputs": {"question": question, "context": context}}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
