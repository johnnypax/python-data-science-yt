import spacy
nlp = spacy.load("it_core_news_sm")

testo = "La lista è una struttura dati molto utilizzata all'interno del linguaggio di programmazione Python"

estrazione = nlp(testo)

for token in estrazione:
    print(token.text, token.pos_, token.dep_)