import spacy
nlp = spacy.load("it_core_news_sm")

testo = "La lista è una struttura dati molto utilizzata all'interno del linguaggio di programmazione Python"

estrazione = nlp(testo)

stack = []                  # Pila contenente tutti i token soggetto

for token in estrazione:    # Popola la pila con solo i token di tipo NOUN e PROPN
    if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
        stack.append(token.text)

if stack:
    output = ''
    while stack:
        output = stack.pop() + ' ' + output
    print(output)