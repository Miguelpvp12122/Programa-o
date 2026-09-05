import random
import time

nome = str(input('diga seu nome: '))
print('xamuel chegou..')

xamuel = int(6)
HP = int(30)
tot = 0
Xamuel_PRIME = int(30)

while True:
    if xamuel <= 0:
        while True:
            if tot == 0:
                print('xamuel é tão fraco tão inutil... Que nem revidar ele consegue')
                time.sleep(1)
                print('XAMUEL NÃO ACEITA MORRE')
                print('XAMUEL USA TODO O SEU PODER PRA AQUENTAR')
                print('Xamuel firou uma alma PRIME')
                print('verdadeira luta começa.')
                time.sleep(1)
                print('xamuel prime: 30 HP, maximo de dano 12')
                print('\n')
                tot += 1
                break
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dadão = dado1 + dado2

        dado1M = random.randint(1, 6)
        dado2M = random.randint(1, 6)
        dadãoM = dado1 + dado2

        Xamuel_PRIME -= dadãoM

        bat = str(input('aperte ENTER pra atacar: '))
        print(f'você da um ataque em xamuel dano {dadão} hp do inimigo {Xamuel_PRIME}')
        

        if Xamuel_PRIME <= 0:
            print('\n')
            print('O ataque foi suficiente...')
            print('xamuel usa seu poder pra se levantar')
            time.sleep(2)
            print('\033[31m')
            print('XAMUEL ESTÁ MAIS FORTE DO QUE ANTES')
            print('XAMUEL MAIS DO QUE PRIME: 1000 HP, maximo de dano 1000. ')
            time.sleep(2)
            print('99999999999999999999999999999999999999999999999999999999999999999999999999')
            print('\033[m')
            print('xamuel morreu...')
            break
            

        print('seu ataque não foi o suficiente hora de xamuel PRIME atacar.')
        HP -= dadãoM
        print(f'ele te deu um soco seu HP está {HP}')


        if HP <= 0:
            print('\n')
            print('você morreu...')
            print(f'{nome} tenha determinação!')
            print('volte em seu save e mate ele')
            print('a sim meu nome é Ch...')
            break
        
while True:
    if xamuel <= 0:
        break
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dadão = dado1 + dado2
    
    bat = str(input('aperte ENTER: '))
    xamuel -= dadão
    print(f'seu dano foi {dadão} a vida do xamuel {xamuel}')
