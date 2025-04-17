# Importazioni di librerie
import spacy
import json

# Caricamento del modello
nlp = spacy.load("it_core_news_sm")

# Leggi il contenuto del file TXT
with open("testo.txt", encoding="utf-8") as file:
    testo = file.read()

# Analisi del testo
estrazione = nlp(testo)

# Estrazione sostantivi
sostantivi = [
    {
        "text": token.text,
        "pos": token.pos_,
        "dep": token.dep_,
        "lemma": token.lemma_,
    } for token in estrazione if token.pos_ in ("NOUN", "PROPN")
]

with open("sostantivi.json", "w", encoding="utf-8") as output:
    json.dump(sostantivi, output, indent=4, ensure_ascii=False)

print("Operazione effettuata con successo!")