# Simple translation System Using Flask and a local Llama model

## About the Project

This project is a two-part translation system that uses a Flask GUI (Graphical User Interface) and a separate translation server. The translation server utilizes the Hugging Face `transformers` library and the `SnypzZz/Llama2-13b-Language-translate` model for local text translation. The system comprises two main components:

1. **Flask GUI (Graphical User Interface):** This part is responsible for the user interface where users can input text, select source and target languages, and receive the translation result.
2. **Translation Server:** A separate server application that accepts HTTP POST requests from the Flask GUI, performs the translation using the local `SnypzZz/Llama2-13b-Language-translate` model, and returns the translation result.

## Operation Principle and HTTP Communication

### Flask GUI

The Flask application serves as the user interface, where users can input text for translation and select source and target languages. It is built using HTML, CSS, and JavaScript, providing a convenient and intuitive user experience.

When a user inputs text and clicks "Translate," a JavaScript function is called, which sends an HTTP POST request to the translation server. This request transmits the text and language selections in JSON format.

### HTTP POST Request

The HTTP POST request is formed and sent using the JavaScript `fetch` function. This function sends the request to the specified URL, in this case, the translation server's address, with the necessary data:

```javascript
fetch('/translate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        text: inputText,
        inputLang: inputLang,
        outputLang: outputLang
    }),
})
```

### Translation Server

The translation server, created using FastAPI, is a separate process that listens for HTTP POST requests. When the server receives a request from the Flask GUI, it parses the JSON data, performs the translation using the Hugging Face `transformers` library and the local `SnypzZz/Llama2-13b-Language-translate` model.

The FastAPI server accepts the text and language codes, performs the translation, and returns the translated text back to the Flask GUI as an HTTP response:

```python
@app.post("/translate")
async def translate(request: TranslationRequest):
    translated_text = translator.translate(request.text, request.source_language, request.target_language)
    return {"translated_text": translated_text}
```

### Data Return to Flask GUI

When the translation server returns a response, the JavaScript `fetch` function receives this response and updates the user interface to display the translated text. This occurs asynchronously, ensuring the user interface remains responsive while waiting for the response.

```javascript
.then(data => {
    document.getElementById('outputText').value = data.translated_text;
})
```

### Communication Scheme

1. **Flask GUI → Translation Server:** The user inputs text and clicks "Translate." The Flask GUI sends an HTTP POST request with the text and language codes to the translation server.
2. **Translation Server → Flask GUI:** The translation server processes the request, performs the translation, and sends the response back to the Flask GUI.
3. **Result Display:** The Flask GUI receives the response and displays the translated text to the user.

This HTTP communication ensures that data exchanges between the Flask GUI and the translation server are fast, efficient, and secure. It also provides flexibility for further system development and integration.

## Technologies

- **Backend:** Flask, FastAPI
- **Frontend:** HTML, JavaScript, CSS
- **Translation Model:** Hugging Face `SnypzZz/Llama2-13b-Language-translate`

## Using the Local Model

The `SnypzZz/Llama2-13b-Language-translate` model is downloaded and used locally. This ensures faster response times and independence from external APIs.

## Running the System

To run this system:
1. Create a new virtual environment.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install all required libraries.
   ```bash
   pip install -r requirements.txt
   ```
3. Start the translation server.
   ```bash
   python3 translator.py
   ```
4. Start the Flask application.
   ```bash
   python3 app.py
   ```
