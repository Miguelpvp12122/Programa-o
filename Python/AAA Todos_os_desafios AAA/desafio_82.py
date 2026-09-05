lista = []
listaP = list()
listaI = list()


while True:
    num = lista.append(int(input('digite um numero: ')))
    continuar = str(input('quer continuar? [S/N]: '))

    if continuar in 'Nn':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listaP.append(v)
    elif v % 2 == 1:
        listaI.append(v)

print(lista, listaP, listaI)

