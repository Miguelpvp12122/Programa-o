import time

def maior(lista):
    tot = 0
    print('analisando os valores passados...')
    time.sleep(1)

    if len(lista) > 0:
        for p in lista:
            print(f'{p} ', end='', flush=True)
            if len(lista) > 1:
                tot += 1
            time.sleep(0.5)


    print(f'ao todo foi informado {tot} valores')
    print(f'o maior valor foi {max(lista)}')
    print('==' * 20)
    print('\n')


lista = [2, 9, 4, 5, 7, 1]
maior(lista)
lista = [4, 7, 0]
maior(lista)
lista = [1, 2]
maior(lista)
lista = [6]
maior(lista)
lista = [0]
maior(lista)
