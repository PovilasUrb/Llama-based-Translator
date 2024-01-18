from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str

class LocalTranslator:
    def __init__(self):
        self.translator = pipeline("translation", model="SnypzZz/Llama2-13b-Language-translate")

    def translate(self, text, source_language, target_language):
        try:
            translation = self.translator(text, src_lang=source_language, tgt_lang=target_language, max_length=400)
            return translation[0]['translation_text']
        except Exception as e:
            return f"Klaida vertimant: {str(e)}"

translator = LocalTranslator()

@app.post("/translate")
async def translate(request: TranslationRequest):
    translated_text = translator.translate(request.text, request.source_language, request.target_language)
    return {"translated_text": translated_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
