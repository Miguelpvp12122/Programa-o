pessoas = list()
dados = list()

tot = totg = totp = 0

while True:
    tot += 1
    dados.append(str(input(f'qual o nome da {tot}ª pessoa? ')))
    dados.append(float(input(f'qual o peso da {tot}ª pessoa? ')))

    if dados[1] <= 70:
        totp += 1
    elif dados[1] > 70:
        totg += 1

    continuar = str(input('quer continuar? [S/N]: '))

    pessoas.append(dados[:])
    dados.clear()

    if continuar == 'N':
        break

print(f'foram {tot} pessoas cadrastadas.')
print(f'existe {totp} com um peso menor do que a media.')
print(f'existe {totg} maior do que a media.')



