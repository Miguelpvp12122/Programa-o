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
        moeda = (f'R${moeda}')
        return moeda
    else:
        return porcento


def moeda(num):
    moeda = float(f'{num}')
    moeda = (f'R${moeda}')
    return moeda
