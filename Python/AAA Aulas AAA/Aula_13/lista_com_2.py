lista = list()
dado = list()

tot = 0

for p in range(0, 3):
    tot += 1
    dado.append(str(input(f'digite o nome da {tot}ª pessoa: ')))
    dado.append(int(input(f'e a idade da {tot}ª pessoa: ')))

    lista.append(dado[:])

    dado.clear()

tot = 0

for t in lista:
    tot += 1
    print(f'nome {tot}ª:  {t[0]}')
    print(f'idade {tot}ª: {t[1]}')
