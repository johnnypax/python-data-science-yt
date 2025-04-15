# Importazione della libreria SpaCy
import spacy

# Caricamento del modello italiano
nlp = spacy.load("it_core_news_sm")

# Frase da analizzare
testo = "La lista è una struttura dati molto utilizzata all'interno del linguaggio di programmazione Python"

# Analisi
estrapolazione = nlp(testo)

# Creo un dizionario con le informazioni linguistiche estratte
analisi = {}

for token in estrapolazione:
    analisi[token.text] = {
        "pos": token.pos_, 
        "dep": token.dep_
    }

# print(analisi)

# Output totale
# for parola, info in analisi.items():
#     print(f"{parola:20} - POS: {info['pos']:10} DEP: {info['dep']}")

# Analisi dei sostantivi
sotantivi = {k: v for k, v in analisi.items() if v["pos"] in ("NOUN", "PROPN")}
print(sotantivi)

for parola, info in sotantivi.items():
    print(f"{parola:20} - POS: {info['pos']:10} DEP: {info['dep']}")