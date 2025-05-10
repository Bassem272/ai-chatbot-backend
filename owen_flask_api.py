from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Use your environment variable or directly paste the key
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://router.huggingface.co/nebius/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    role = data.get("role")
    content = data.get("content")

    if not role or not content:
        return jsonify({"error": "Missing role or content "}), 400

    payload = {
        "messages": [{"role": role, "content": content}],
        "model": "Qwen/Qwen3-30B-A3B-fast",
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    result = response.json()

    return result


if __name__ == "__main__":
    app.run(debug=True)
