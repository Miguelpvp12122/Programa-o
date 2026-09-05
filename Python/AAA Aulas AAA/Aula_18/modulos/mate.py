def soma(a = 0, b = 0):
    '''
     -> soma os 2 numeros
    a = numero 1
    b = numero 2
    '''
    c = a + b

    return c


def sub(a = 0, b = 0, MM=False):
    '''
     -> subtrai os 2 numeros
    a = numero 1
    b = numero 2

    MM = True
    * faz a regra do maior e menor
    '''

    if MM == False:
        c = a - b

    elif MM == True:
        if a > b:
            c = a - b
        else:
            c = b - a

    return c


def mul(a = 0, b = 0):
    '''
     -> Multiplica os 2 numeros
    a = numero 1
    b = numero 2
    '''

    c = a * b

    return c

def div(a = 0, b = 0, MM=False):
    '''
     -> dividi os 2 numeros
    a = numero 1
    b = numero 2

    MM = True
    * faz a regra do maior e menor
    '''

    if MM == False:
        c = a / b

    elif MM == True:
        if a > b:
            c = a / b
        else:
            c = b / a

    return c
