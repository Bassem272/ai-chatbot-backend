from flask import Flask , request, jsonify
from transformers import pipeline 

app = Flask(__name__)
# Load question-answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question")
    context = data.get("context")

    if not question or not context:
        return jsonify({"error": "Missing question or context"}), 400

    result = qa_pipeline(question= question, context= context)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)