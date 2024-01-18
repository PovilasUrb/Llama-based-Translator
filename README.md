# Vertimo Sistema Su Flask ir Hugging Face

## Apie projektą

Šis projektas yra dviejų dalių vertimo sistema, kuri naudoja Flask GUI (grafinei vartotojo sąsajai) ir atskirą vertimo serverį. Vertimo serveris naudoja Hugging Face `transformers` biblioteką ir `SnypzZz/Llama2-13b-Language-translate` modelį lokaliam teksto vertimui. Sistemą sudaro du pagrindiniai komponentai:

1. **Flask GUI (Grafinei Vartotojo Sąsajai):** Ši dalis yra atsakinga už vartotojo sąsają, kurioje galima įvesti tekstą, pasirinkti šaltinio ir tikslinę kalbas bei gauti vertimo rezultatą.

2. **Vertimo Serveris:** Atskira serverio aplikacija, kuri priima HTTP POST užklausas iš Flask GUI, atlieka vertimą naudojant lokalų `SnypzZz/Llama2-13b-Language-translate` modelį ir grąžina vertimo rezultatą.

## Veikimo Principas ir Komunikacija per HTTP

### Flask GUI

Flask aplikacija yra vartotojo sąsaja, kurioje galima įvesti tekstą vertimui, pasirinkti šaltinio ir tikslinę kalbas. Ji yra sukurta naudojant HTML, CSS ir JavaScript, leidžianti patogų ir intuityvų vartotojo patirtį.

Kai vartotojas įveda tekstą ir paspaudžia "Versti", JavaScript funkcija yra iškviečiama, kuri siunčia HTTP POST užklausą į vertimo serverį. Ši užklausa perduoda tekstą ir kalbų pasirinkimus JSON formatu.

### HTTP POST Užklausa

HTTP POST užklausa yra suformuojama ir išsiunčiama naudojant JavaScript `fetch` funkciją. Ši funkcija siunčia užklausą į nurodytą URL, šiuo atveju vertimo serverio adresą, su reikalingais duomenimis:

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

### Vertimo Serveris

Vertimo serveris, sukuriamas naudojant FastAPI, yra atskiras procesas, kuris klausosi HTTP POST užklausų. Kai serveris gauna užklausą iš Flask GUI, jis išanalizuoja JSON duomenis, atlieka vertimą naudodamas Hugging Face `transformers` biblioteką ir lokalų `SnypzZz/Llama2-13b-Language-translate` modelį.

FastAPI serveris priima tekstą ir kalbų kodus, atlieka vertimą ir grąžina išverstą tekstą atgal į Flask GUI kaip HTTP atsakymą:

```python
@app.post("/translate")
async def translate(request: TranslationRequest):
    translated_text = translator.translate(request.text, request.source_language, request.target_language)
    return {"translated_text": translated_text}
```

### Duomenų Grąžinimas į Flask GUI

Kai vertimo serveris grąžina atsakymą, JavaScript funkcija `fetch` gauna šį atsakymą ir atnaujina vartotojo sąsają, rodydama išverstą tekstą. Tai vyksta asinchroniškai, todėl vartotojo sąsaja lieka atsako laukimo metu reaktyvi.

```javascript
.then(data => {
    document.getElementById('outputText').value = data.translated_text;
})
```

### Komunikacijos Schema

1. **Flask GUI → Vertimo Serveris:** Vartotojas įveda tekstą ir paspaudžia "Versti". Flask GUI siunčia HTTP POST užklausą su tekstu ir kalbų kodais į vertimo serverį.
2. **Vertimo Serveris → Flask GUI:** Vertimo serveris apdoroja užklausą, atlieka vertimą ir siunčia atsakymą atgal į Flask GUI.
3. **Rezultatų Atvaizdavimas:** Flask GUI gauna atsakymą ir atvaizduoja išverstą tekstą vartotojui.

Ši komunikacija per HTTP užtikrina, kad duomenų mainai tarp Flask GUI ir vertimo serverio yra greiti, efektyvūs ir saugūs. Taip pat suteikia lankstumą tolesnei sistemos plėtrai ir integravimui.
## Technologijos

- **Backend:** Flask, FastAPI
- **Frontend:** HTML, JavaScript, CSS
- **Vertimo Modelis:** Hugging Face `SnypzZz/Llama2-13b-Language-translate`

## Lokalus Modelio Naudotojimas

`SnypzZz/Llama2-13b-Language-translate` modelis atsisiunčiamas ir naudojamas lokaliai. Tai leidžia užtikrinti greitesnį atsako laiką ir nepriklausomybę nuo išorinių API.

## Paleidimas

Norėdami paleisti šią sistemą:
1. Sukurkite nauja virtualu environmenta.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Įdiekite visas reikalingas bibliotekas.
   ```bash
   pip install -r requirements.txt
   ```
3. Paleiskite `translator.py`.
   ```bash
   python3 translator.py
   ```
4. Paleiskite `main.py` Flask aplikaciją.
   ```bash
   python3 app.py
   ```

