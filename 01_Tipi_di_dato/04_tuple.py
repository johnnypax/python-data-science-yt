# Tuple differenti
# tupla_stringhe = ("Giovanni", "Pace")
# tupla_numeri = (1, 2, 3)
# tupla_mista = ("Giovanni", "Pace", 38, True)
# tupla_singola = ("Giovanni",)

# print(tupla_stringhe)
# print(tupla_numeri)
# print(tupla_mista)
# print(tupla_singola)

# Recupero delle informazioni tupla
# tupla_mista = ("Giovanni", "Pace", 38, True)
# print( tupla_mista[0] )
# print( tupla_mista[2] )

# Riassegnazione non disponibile
# tupla_mista = ("Giovanni", "Pace", 38, True)
# tupla_mista[0] = "Mario";     # Non consentito

# Scansione di una tupla
# tupla_mista = ("Giovanni", "Pace", 38, True)
# for item in ("Giovanni", "Pace", 38, True):
#     print(item)

# for item in ("Giovanni", "Pace", 38, True):
#     print(item)

# Lunghezza di una tupla
# tupla_mista = ("Giovanni", "Pace", 38, True)
# print("Lunghezza tupla: ", len(tupla_mista))

# Unpacking
# persona = ("Giovanni", "Pace", 38, True)
# nome, cognome, eta, hasPatente = persona

# print("Nome:", nome)
# print("Cognome:", cognome)
# print("Età:", eta)
# print("Ha la patente:", hasPatente)

# Tupla come tipo di ritorno
# def dettaglioPersona():
#     return ("Giovanni", "Pace", 38, True)

# nome, cognome, eta, hasPatente = dettaglioPersona()
# print("Nome:", nome)
# print("Cognome:", cognome)
# print("Età:", eta)
# print("Ha la patente:", hasPatente)

todo = [("Sveglia", "08:00"),("Colazione", "08:30"),("Lavoro", "09:00")]

# print(todo)

# for item in todo:
#     print(item[0])

print(todo[2][1])