# 🧠 Question Answering with Flask and Transformers

This project contains **two Flask-based servers** that demonstrate how to use a pre-trained question-answering model (`deepset/roberta-base-squad2`) in two different ways:

- 🔌 **Locally** using Hugging Face's `transformers` pipeline
- ☁️ **Remotely** using the Hugging Face Inference API

---

## 📁 Project Structure

```

.
├── qa_flask_local.py       # Uses the model locally with transformers
├── qa_flask_api.py         # Uses the Hugging Face Inference API
├── .env                  # Stores your Hugging Face API token (not committed)
├── requirements.txt         # Example of .env file
└── README.md             # Project documentation

````

---

## 🚀 Requirements

Install required packages using:

```bash
pip install flask transformers requests python-dotenv
````

---

## 🔐 Environment Variables

For the API-based server, you need a Hugging Face API token.

1. Create a `.env` file in the project root:

```
HF_API_KEY=your_huggingface_api_token_here
```

2. An example file is included as `.env.example`.

3. Make sure your `.env` file is **never committed** to version control.

---

## 🔌 Option 1: Local Model Server

**File**: `qa_flask_local.py`

This version loads the QA model directly on your machine.

### ✅ Use When:

* You have enough resources to load the model locally.
* You want faster inference without rate limits.

### 🔧 How to Run:

```bash
python qa_flask_local.py
```

### 🧪 Test the Endpoint

You can send a POST request to:

```
http://127.0.0.1:5000/ask
```

With a JSON body like:

```json
{
  "question": "What is the capital of France?",
  "context": "France's capital is Paris, which is known for the Eiffel Tower."
}
```

---

## ☁️ Option 2: Hugging Face API Server

**File**: `qa_flask_api.py`

This version uses the Hugging Face hosted inference API.

### ✅ Use When:

* You don't want to load the model locally.
* You're okay with depending on internet/API access.

### 🔧 How to Run:

1. Ensure your `.env` file has the correct token.
2. Run the server:

```bash
python qa_flask_api.py
```

### 🧪 Test the Endpoint

Same as above:

```
http://127.0.0.1:5000/ask
```

With the same JSON payload.

---

## 🧹 Good Practices

* Keep `.env` files secret.
* Use `qa_flask_local.py` in development or offline setups.
* Use `qa_flask_api.py` for lightweight clients or quick tests.

---

## 📌 License

This project is for educational purposes. Refer to the Hugging Face and Transformers license terms for model usage.

---

## 🧑‍💻 Bassem Gehad

Made with ❤️ using Flask and 🤗 Transformers.


