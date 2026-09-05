def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True

        else:
            print('\033[31mERRO DIGITE UM NUMERO\033[m')
        
        if ok == True:
            break

    return valor


vari = leiaint('digite um numero: ')
print(f'{vari} foi o numero que você digitou')
