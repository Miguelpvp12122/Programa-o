def metade(num, fom=False):
    meta = num / 2
    if fom == True:
        moeda = float(f'{meta}')
        moeda = (f'R${moeda}')
        return moeda
    else:
        return meta


def dobro(num, fom=False):
    dobro = num + num
    if fom == True:
        moeda = float(f'{dobro}')
        moeda = (f'R${moeda}')
        return moeda
    else:
        return dobro


def aumentar(num, por=0, fom=False):
    porcento = num + (num * por / 100)
    if fom == True:
        moeda = float(f'{porcento}')
        moeda = (f'R${moeda}')
        return moeda
    else:
        return porcento


def diminuir(num, por=0, fom=False):
    porcento = num - (num * por / 100)
    if fom == True:
        moeda = float(f'{porcento}')
        moeda = (f'R${moeda:>.2f}')
        return moeda
    else:
        return porcento


def moeda(num):
    moeda = float(f'{num}')
    moeda = (f'R${moeda:>.2f}')
    return moeda

     
def resumo(num):
    print('==================================================')
    print('Resumo do Valor:')
    print('==================================================')
    print('')
    print('==================================================')
    print(f'Preço analizado:    {moeda(num)}')
    print(f'Metade do preço:    {(metade(num, True))}')
    print(f'dobro do valor:     {(dobro(num, True))}')
    print(f'80% de aumento:     {(aumentar(num, 80, True))}')
    print(f'35% de redução:     {(diminuir(num, 35, True))}')
    print('==================================================')
