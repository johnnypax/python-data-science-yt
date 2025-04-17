import pandas as pd
import numpy as np

tabella = {
    'Nome': ['Giovanni', 'Valeria', 'Marika'],
    'Eta': [38, 19, 39],
    'Citta': ['L\'Aquila', np.nan, 'Chieti']
}

df = pd.DataFrame(tabella)
# print(df)

# Operazioni semplici
# print( df['Nome'][0] )      # Accedo prima alla colonna e poi alla riga!
# print( df.iloc[0] )         # Restituisci la riga all'indice 0
# print( df.loc[1, 'Citta'] )     # Accesso alla cella specifica in modalità esplicita

# Operazione utile
# print( df.describe() )      # Accesso alle statistiche
# print( df.info() )          # Statistiche sui dati
# print( df['Eta'].mean() )
# print( df.head(2) )
# print( df.tail(1) )

# Filtri
# print( df[df['Eta'] > 30] )
# print( df[df['Citta'] == 'Chieti'])

# Esportazione in CSV
# df.to_csv('esportazione.csv', index=True)

# Leggere un CSV
dataFrame = pd.read_csv('esportazione.csv')
print(dataFrame)