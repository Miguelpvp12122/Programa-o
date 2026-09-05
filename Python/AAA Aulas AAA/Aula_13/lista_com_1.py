lista1 = ['Ezequiel', 13]
lista2 = ['Gabryel', 13]
lista3 = ['Miguel', 13]
lista4 = ['José', 14]
lista5 = ['Ruan', 14]

tot = 0

garela = list()

garela.append(lista1[:])
garela.append(lista2[:])
garela.append(lista3[:])
garela.append(lista4[:])
garela.append(lista5[:])

print(garela[4][0])

#ou

for p in garela:
    tot += 1
    print(f'o nome da {tot}ª pessoa é {p[0]} e a idade é {p[1]}')