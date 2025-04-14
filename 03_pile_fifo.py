# coda = []

# # Aggiunta in fondo (ENQUEUE)
# coda.append("Giovanni")
# coda.append("Valeria")
# coda.append("Mario")
# coda.append("Marika")

# # Rimozione dal fronte (DEQUEUE) - NAIVE
# persona = coda.pop(0)
# print("Estratto: ", persona)
# print(coda)

# -----------------------------------------------------

from collections import deque

coda = deque()

# ENQUEUE
coda.append("Giovanni")
coda.append("Valeria")
coda.append("Mario")
coda.append("Marika")

# DEQUEUE
# persona = coda.popleft()              # .pop()
# print("Estratto: ", persona)
# print(coda)

# Svuota la coda
# coda.clear()
# print(coda)

coda.appendleft("Ester")
print(coda)
