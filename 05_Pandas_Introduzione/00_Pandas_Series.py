import pandas as pd

# Serie con indice automatico
# persone = ["Giovanni", "Valeria", "Mario"]
# invitati = pd.Series(persone)
# print(invitati)

# Serie con indice personalizzato
numeri = pd.Series([5,6,98,6,354], index=['a', 'b', 'c', 'd', 'e'])
# print(numeri)

# Operazioni sulle series
# print(numeri['b'])
# print( numeri + 5 )
# print( numeri * 5 )
print( numeri.mean() )
print( numeri.min() )
print( numeri.max() )