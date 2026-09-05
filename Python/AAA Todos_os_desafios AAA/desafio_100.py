import time
import random

def sorteie(list):
    for p in range(0, 5):
        ramdum = random.randint(1, 10)
        list.append(ramdum)

        print(f'{ramdum} ', end='', flush=True)
        time.sleep(0.5)
    print('Terminado...')

def soma(list, par):
    for p in list:
        if p % 2 == 0:
            par.append(p)
    print(f'a soma dos numeros pares é {sum(par)}')



lista = []
par = []
sorteie(lista)
soma(lista, par)
