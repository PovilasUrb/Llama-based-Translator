function translateText() {
    const inputText = document.getElementById('inputText').value;
    const inputLang = document.getElementById('inputLang').value;
    const outputLang = document.getElementById('outputLang').value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({text: inputText, inputLang: inputLang, outputLang: outputLang}),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputText').value = data.translated_text;
    })
    .catch(error => console.error('Error:', error));
}
