cont = 0
num = int(input('digite um numero pra ver sua tabuada: '))
while True:
    cont += 1
    nume = num * cont
    print(f'{num} X {cont} = {nume}')
    if cont == 10:
        cont -= 10
        num = int(input('quer mais uma tabuada? se sim digite: '))
    if num < 0:
        print('pograma finalizado.')
        break
    