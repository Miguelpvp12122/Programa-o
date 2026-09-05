lista = []

Continue = ''

while Continue != 'N':
    numero = int(input('digite um numero: '))
    if numero not in lista:
        lista.append(numero)
        print('numero adicionado')
    else:
        print('o numero ja está na lista')
    
    Continue = str(input('quer continuar? [S/N]: '))


lista.sort()
print(lista)