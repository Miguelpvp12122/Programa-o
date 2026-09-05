# Tuplas são imutaveis

lache = ('Gabryel', 'Edson', 'Ruan', 'José', 'Ezequiel')

for solei in range(0, len(lache)):
    print(f'eu solei {lache[solei]} na posisão {solei}')

for solei, comida in enumerate(lache):
    print(f'eu ganhei de {comida} na posição {solei}')
print('azhei facizl')