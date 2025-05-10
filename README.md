# Simple Flask Server for Interacting with the `deepset/roberta-base-squad2` Model

This project is a simple Flask server that allows you to interact with the **`deepset/roberta-base-squad2`** question-answering model from Hugging Face's `transformers` library. The model is capable of answering questions based on a provided context.

## Project Overview

This Flask server exposes a single endpoint (`/ask`) that accepts a **POST** request containing a question and context. The model processes the request and returns the most likely answer from the context.

### Model Information

- **Model Name**: `deepset/roberta-base-squad2`
- **Model Type**: Question-Answering
- **Model Size**: ~500MB
- **Model Source**: [Hugging Face Model Hub](https://huggingface.co/deepset/roberta-base-squad2)


## Installation

1. **Clone the repository**:

   git clone https://github.com/your-repo/simple-flask-server.git
   cd simple-flask-server


2. **Create and activate a virtual environment**:

   * On **Windows**:

 
     python -m venv venv
     venv\Scripts\activate


   * On **macOS/Linux**:


     python3 -m venv venv
     source venv/bin/activate


3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the model locally**:
   When the Flask server runs for the first time, it will automatically download the **`deepset/roberta-base-squad2`** model. This model is **\~500MB** in size, and the model files will be stored in your local cache (e.g., `~/.cache/huggingface` on Unix systems or `C:\Users\<user>\.cache\huggingface` on Windows).

---

## Running the Flask Server

To start the server:

```bash
python app.py
```

By default, the server will run on [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage Instructions

Once the Flask server is running, you can interact with the model by sending a **POST** request to the `/ask` endpoint.

### Example Request using **Postman** or **cURL**:

#### Endpoint: `POST /ask`

* **Headers**:

  * Content-Type: `application/json`

#### Request Body:

```json
{
  "question": "What is AI?",
  "context": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. AI is used in various applications, such as speech recognition, problem-solving, and learning."
}
```

#### Example using **cURL**:

```bash
curl -X POST http://127.0.0.1:5000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is AI?\", \"context\": \"Artificial Intelligence (AI) refers to the simulation of human intelligence in machines. AI is used in various applications, such as speech recognition, problem-solving, and learning.\"}"
```

#### Expected Response:

```json
{
  "answer": "simulation of human intelligence",
  "start": 57,
  "end": 88,
  "score": 0.963
}
```

* **`answer`**: The model's best guess for the answer within the provided context.
* **`start`**: The index of the start of the answer in the context.
* **`end`**: The index of the end of the answer in the context.
* **`score`**: The confidence score of the model's answer.

---

## Troubleshooting

* If you encounter issues with the model download (e.g., low disk space), ensure you have sufficient space in your cache directory. You can adjust the location of the Hugging Face cache by setting the `HF_HOME` environment variable.
* The server may take time to load the model on the first run. Once the model is downloaded, subsequent requests will be faster.

---

## Notes

* **Model Size**: \~500MB (stored locally after the first download)
* This project is for educational and testing purposes.
* It is recommended not to use the Flask development server in production. For production environments, consider using a WSGI server like Gunicorn.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

Now, the entire `README.md` is in a single markdown block as you requested. Let me know if you need further adjustments!
```
