numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'desseseiz', 'dessete', 'dezoito', 'dessenove', 'vinte')

tot = 0

pergunta = int(input('digite um numero de 0 a 20: '))

while pergunta != numeros:
    if pergunta < 0:
        pergunta = int(input('por favor digite um numero de 0 a 20: '))
    elif pergunta > 20:
        pergunta = int(input('por favor digite um numero de 0 a 20: '))
    else:
        print(f'o numero que você digitou foi {numeros[pergunta]}')
        tot += 1
        break

if tot == 0:
    print(f'o numero que você digitou foi {numeros[pergunta]}')
