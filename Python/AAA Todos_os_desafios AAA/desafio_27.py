import random

computador = random.randint(0,3)

pergunta = int(input('escolha um numero de 1 a 5: '))

if pergunta == computador:
    print('voce ganhou!!!')
else:
    print(f'naverdade pensei no numero {computador}')

