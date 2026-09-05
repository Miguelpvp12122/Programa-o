x3 = [[], [], []]
dados = list()
Mm = list()

tot1 = 0
tot2 = 0
tot3 = 0
tot4 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    tot3 += dados[0]

    if p == 2:
        tot4 += dados[0]

    elif p == 1:
        Mm.append(dados[0])

    x3[0].append(dados[:])
    dados.clear()


tot1 += 1
tot2 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    tot3 += dados[0]

    if p == 2:
        tot4 += dados[0]

    elif p == 1:
        Mm.append(dados[0])

    x3[1].append(dados[:])
    dados.clear()

tot1 += 1
tot2 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    tot3 += dados[0]

    if p == 2:
        tot4 += dados[0]

    elif p == 1:
        Mm.append(dados[0])

    x3[2].append(dados[:])
    dados.clear()

for p in range(0,1):
    print(f'[{x3[0][0]}] [{x3[0][1]}] [{x3[0][2]}]')
    print(f'[{x3[1][0]}] [{x3[1][1]}] [{x3[1][2]}]')
    print(f'[{x3[2][0]}] [{x3[2][1]}] [{x3[2][2]}]')

print(f'a soma entre todos os valores foi {tot3}')
print(f'a soma da terceira coluna foi {tot4}')
print(f'o maior valor da segunda linha é {max(Mm)}')
