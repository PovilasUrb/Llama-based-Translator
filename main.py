from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.json['text']
    input_lang = request.json['inputLang']
    output_lang = request.json['outputLang']
    
    # Siunčia užklausą į vertimo serverį
    response = requests.post("http://localhost:8000/translate", json={
        "text": input_text,
        "source_language": input_lang,
        "target_language": output_lang
    })

    translated_text = response.json().get("translated_text", "Vertimo klaida.") if response.status_code == 200 else "Serverio klaida."

    return jsonify(translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
