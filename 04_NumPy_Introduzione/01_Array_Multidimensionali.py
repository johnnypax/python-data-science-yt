import numpy as np

# Stipendi
salario_gio = [3000, 2800, 2600, 3000, 2500]
salario_val = [3300, 2900, 2800, 3100, 2320]
salario_mar = [8500, 1800, 6600, 8000, 2530]

riep_salari = np.array([salario_gio, salario_val, salario_mar])

# Bonus
bonus_gio = [100, 100, 200, 100, 500]
bonus_val = [300, 900, 800, 100, 320]
bonus_mar = [800, 800, 600, 100, 530]

riep_bonus = np.array([bonus_gio, bonus_val, bonus_mar])

# Operazioni semplici tra matrici np, + *
riepilogo = riep_salari + riep_bonus
# print(type(riepilogo), riepilogo)

# Funzioni statistiche
# print( riepilogo.max() )

print( np.amax(riepilogo) )

#Ricerca per singolo asse
print( np.amax(riepilogo, axis=0) )
print( np.amax(riepilogo, axis=1) )