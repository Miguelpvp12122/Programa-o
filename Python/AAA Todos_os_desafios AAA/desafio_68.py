import random
V = 0


while True:
    comp = random.randint(0, 5)
    num = int(input('digite um numero de 5 a 0: '))
    PI = str(input('qual você escolhe escolhe? [P/I]: '))


    soma = num + comp
    div = soma % 2


    if PI == 'I' or 'i':
        if div == 1:
            print('você ganhou!')
            print('mais 1 ponto de vitoria!')
            V += 1
        elif div == 0:
            print('o computador ganhou.')
            print(f'você ganhou {V} vezes seguidas.')
            break


    elif PI == 'P' or 'p':
        if div == 1:
            print('o computador ganhou.')
            print(f'você ganhou {V} vezes seguidas.')
            break
        if div == 0:
            print('você ganhou!')
            print('mais 1 ponto de vitoria!')
            V += 1
    