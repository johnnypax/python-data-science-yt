# Rimozione del duplicato
# frutta = {"Mela", "Pera", "Mela"}
# print(frutta)

# Set dalla lista
# numeri = set( [1,2,3,4,5] )
# print(numeri)

# Aggiunta di elementi nel SET
# elenco = set()

# elenco.add("Mario")
# elenco.add("Giovanni")
# elenco.add("Mario")

# print(elenco)

persone = {"Giovanni", "Mario", "Valeria"}

# Rimozione con Exception se non esiste
# persone.remove("Marika")
# print(persone)

# Rimozione sicura
# persone.discard("Marika")
# print(persone)

# elemento = persone.pop()
# print(elemento)

# -------------------------------------------------

a = {"Giovanni", "Mario", "Valeria"}
b = {"Valeria", "Mela", "Ananas"}

# Unione
print( a | b )

# Intersezione
print( a & b )

# Differenza
print( a - b )

# Diff. Simmetrica
print( a ^ b )

# -----------------------------------------

# Frozen Set
frozen = frozenset(["Mela", "Banana", "Mela"])
print(frozen)

