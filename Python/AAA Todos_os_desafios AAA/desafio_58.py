import random

ND = int(input('Eu vou pensar num numero de 1 a 10 tente adivinhar! '))

computador = random.randint(1, 10)

zero = int(1)

while ND != computador:
    ND = int(input('Errou! Ainda estou pensando no mesmo numero, tente denovo: '))
    zero += 1

print(f'A você acertou! precisou de {zero} pra acerta ')
if zero == '1':
    print('SLK TU É UM GENIO')
elif zero == '5':
    print('demorou em?')
elif zero == '10':
    print('como você errou tanto?')
elif zero == '25':
    print('OK OK você foi longe ATE DEMAIS como errou mais doque 20 VEZES CARA')
elif zero == '40':
    print('so uma coisa a dizer COMOOOOOOOOOOOO')