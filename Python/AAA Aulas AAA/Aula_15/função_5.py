import time

def soma():
    a = int(input('digite 1 numero: '))
    b = int(input('digite o segundo numero: '))
    s = a + b
    print(f'a soma deles foi {s}')

def lin():
    print('=='*30)

def tmp():
    time.sleep(1)
    print('\n')



lin()
soma()
lin()
tmp()

lin()
soma()
lin()
