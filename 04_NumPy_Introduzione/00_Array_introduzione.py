import numpy as np

uno = np.array([2,6,8])
due = np.array([9,5,6])

print("Somma", uno + due)
print("Prodotto", uno * due)
print("Elevazione al quadrato", uno ** 2)
print("Prodotto scalare", np.dot(uno, due))
