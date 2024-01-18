# Vertimo Sistema Su Flask ir Hugging Face

## Apie projektą

Šis projektas yra dviejų dalių vertimo sistema, kuri naudoja Flask GUI (grafinei vartotojo sąsajai) ir atskirą vertimo serverį. Vertimo serveris naudoja Hugging Face `transformers` biblioteką ir `Llama2-13b-Language-translate` modelį lokaliam teksto vertimui. Sistemą sudaro du pagrindiniai komponentai:

1. **Flask GUI (Grafinei Vartotojo Sąsajai):** Ši dalis yra atsakinga už vartotojo sąsają, kurioje galima įvesti tekstą, pasirinkti šaltinio ir tikslinę kalbas bei gauti vertimo rezultatą.

2. **Vertimo Serveris:** Atskira serverio aplikacija, kuri priima HTTP POST užklausas iš Flask GUI, atlieka vertimą naudojant lokalų `SnypzZz/Llama2-13b-Language-translate` modelį ir grąžina vertimo rezultatą.

## Kaip tai veikia

- Vartotojas naudoja Flask GUI įveda tekstą ir pasirenka šaltinio bei tikslinę kalbas.
- Flask GUI siunčia HTTP POST užklausą į vertimo serverį su tekstu ir kalbų informacija.
- Vertimo serveris gauna užklausą, naudoja `SnypzZz/Llama2-13b-Language-translate` modelį teksto vertimui ir grąžina išverstą tekstą atgal į Flask GUI.
- Flask GUI pateikia vertimo rezultatą vartotojui.

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

## Licencija

[MIT](LICENSE) - ši licencija leidžia laisvai naudoti, kopijuoti, keisti ir platinti šį projektą. 

---

Projektas sukurtas siekiant suteikti efektyvų ir patogų būdą atlikti teksto vertimus naudojant šiuolaikines technologijas ir modelius. Jis gali būti naudojamas kaip mokymosi priemonė arba kaip pagrindas tolesnei plėtrai ir pritaikymui individualiems poreikiams.
