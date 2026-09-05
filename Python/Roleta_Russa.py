import random
import time

def dizer(bala):
    if bala == 1:
        print('A bala é verdadeira')
    else:
        print('A bala é falsa')

def prox():
    global Prox_bala

    if Prox_bala == Bala_1:
        Prox_bala = Bala_2
        print('a1')

    elif Prox_bala == Bala_2:
        Prox_bala = Bala_3
        print('a2')

    elif Prox_bala == Bala_3:
        Prox_bala = Bala_4
        print('a3')

    elif Prox_bala == Bala_4:
        Prox_bala = Bala_5
        print('a4')

    elif Prox_bala == Bala_5:
        print('a5')
    
    return


VER = 0
FAL = 0

Bala_1 = random.randint(1 ,2)
Bala_2 = random.randint(1 ,2)
Bala_3 = random.randint(1 ,2)
Bala_4 = 1
Bala_5 = random.randint(1, 2)

if Bala_1 == 1:
    VER += 1
else:
    FAL += 1


if Bala_2 == 1:
    VER += 1
else:
    FAL += 1


if Bala_3 == 1:
    VER += 1
else:
    FAL += 1

if Bala_4 == 1:
    VER += 1
else:
    FAL += 1


if Bala_5 == 1:
    VER += 1
else:
    FAL += 1


Prox_bala = Bala_1

print(f'Na rodada terá {VER} verdadeiras e {FAL} falsas')


while True:
    tiro = int(input('Atirar no inimigo ou em se mesmo: '))

    prox()
    print(Prox_bala)


    if tiro == 1:
        if Bala_1 == 1:
            print('Você morreu')
            Prox_bala = Bala_2
            break

        if Bala_1 == 2:
            print('Era falsa')
            Prox_bala = Bala_2

    elif tiro == 2:
        if Bala_1 == 1:
            print('Você mata o inimigo')
            Prox_bala = Bala_2
            break

        if Bala_1 == 2:
            print('Era falsa')
            Prox_bala = Bala_2
            break

    elif tiro == 3:
        dizer(Bala_1)
    
    print('\n')
    

