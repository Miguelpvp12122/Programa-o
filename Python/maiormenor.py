n = int(input('digite um numero: '))

maior = 0

menor = 0

cont = 0

cont += 1

if cont == 1:
    maior = menor = n
else:
    if n > maior:
        maior = n
    elif n < maior:
        menor = n
        

