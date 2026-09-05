totma = 0
totfe = 0
totfe2 = 0

contma = 0
contfe = 0

while True:
    print('='*10, 'casdratos de pessoas', '='*10)
    
    idade = int(input('quantos anos tem a pessoa? '))
    print('='*42)
    sexo = str(input('qual o sexo da pessoa? [M/F]: '))
    print('='*42)
    continuar = str(input('quer continuar? [S/N]: '))
    print('='*42)
    print('\n')

    if sexo == 'M':
        contma += 1
        idadeM = idade - 18
        if idadeM >= 1:
            totma += 1
    elif sexo == 'F':
        contfe += 1
        idadeF = idade - 20
        idadeF2 = idade - 18
        if idadeF >= 1:
            totfe += 1
        elif idadeF2 >= 1:
            totfe2 += 1

    totT = totfe2 + totma

    if continuar == 'N':
        print(f'total de pessoa com mais de 18 anos: {totT}')
        print(f'total de homens cadrastados {contma}')
        print(f'total de mulheres cadrastadas {contfe}')
        print(f'total de mulheres com mais de 20 anos {totfe}')
        print(f'{continuar}')
        break
    elif continuar == 'S':
        print('continuando.')
