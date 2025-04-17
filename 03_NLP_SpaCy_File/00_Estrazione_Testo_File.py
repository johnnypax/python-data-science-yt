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

risultato = []
for token in estrazione:
    risultato.append(
        {
            "text": token.text,
            "pos": token.pos_,
            "dep": token.dep_,
            "lemma": token.lemma_,
        }
    )

with open("analisi.json", "w", encoding="utf-8") as output_file:
    json.dump(risultato, output_file, indent=2, ensure_ascii=False)

print("Operazione effettuata con successo!")