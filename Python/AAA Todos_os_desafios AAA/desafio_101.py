import datetime

def voto(ano = 0):
    atual = datetime.date.today().year
    voto = atual - ano
    


    print(f'com {voto} anos o voto é: ')

    if voto < 18:
        print('Não vota', end='')
    if voto >= 18 and voto <= 64:
        print('Voto obrigatorio', end='')
    if voto >= 65:
        print('Voto opcional', end='')


data = int(input('qual sua data de nascimento? '))
voto(data)
