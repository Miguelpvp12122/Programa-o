def leiaint(num):
    while True:
        try:
            n = int(input(num))

        except (ValueError, TypeError):
            print('\033[31mERRO: o valor digitado não está correto!\033[m')
            print('')
        except KeyboardInterrupt:
            n = 0

        else:
            break
    return n

def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        
        except (ValueError, TypeError):
            print('\033[31mERRO: o valor digitado não está correto!\033[m')
            print('')
        except KeyboardInterrupt:
            n = 0.0
        
        else:
            break
    
    return n
    


vari = leiaint('digite um numero: ')
vari2 = leiafloat('digite um numero flutuante: ')

print(f'{vari} foi o numero inteiro que você digitou, e o flutuante foi o numero {vari2}')
