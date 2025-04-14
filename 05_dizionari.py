persona = {
    "nome": "Giovanni",
    "cognome": "Pace",
    "eta": 38,
    "hasPatente": True
}

# Accesso
# print( persona["nome"] )

# nominativo = persona["nome"]
# print(nominativo)

# numero_animali = persona.get("animali", "Non specificato")
# print(numero_animali)

# Modifica
# persona["nome"] = "Valeria"
# print( persona["nome"] )

# Eliminazione
# print(persona)
# del persona["hasPatente"]
# print(persona)

# -----------------------------------------

# Ottenere tutte le chiavi
# chiavi = persona.keys()
# print(chiavi)

# Ottenere tutti i valori
# valori = persona.values()
# print(valori)

# Ottenere tutti gli elementi coppie chiave-val
# elementi = persona.items()
# print(elementi)

# Aggiornamento dei valori delle chiavi
# aggiorna = {
#     "nome": "Valeria",
#     "eta": "35"
# }

# persona.update(aggiorna)
# print(persona)

# Elimina tutte le combinazioni del dictionary
# persona.clear()
# print(persona)

# ----------------------------------------------

# chiavi = persona.keys()
# for item in chiavi:
#     print(item)


# valori = persona.values()
# for item in valori:
#     print(item)

# Accesso interpolato agli elementi
# elementi = persona.items()
# for chiave, valore in elementi:
#     print(f"{chiave}, {valore}")

# --------------------------------------------

from collections import OrderedDict

dizionario = {
    "c": 2,
    "a": 1,
    "b": 3
}

# Ordino rispetto alle chiavi
# diz_ord_chiav = OrderedDict(sorted(dizionario.items()))
# print(diz_ord_chiav)

# Ordino rispetto ai valori
diz_ord_valore = OrderedDict(sorted(dizionario.items(), key=lambda x: x[1]))
print(diz_ord_valore)