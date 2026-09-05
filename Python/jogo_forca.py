letra1 = '_'
letra2 = '_'
letra3 = '_'
letra4 = '_'
letra5 = '_'
letra6 = '_'
letra7 = '_'
letra8 = '_'

tot = 0
tot2 = 5

palavra = letra1 + letra2 + letra3 + letra4 + letra5 + letra6 + letra7 + letra8

print(letra1,letra2,letra3,letra4,letra5,letra6,letra7,letra8, end='')
print('\n')


while True:
    print('='*30)
    print('Jogo da forca')
    print('='*30)
    print('\n')
    letras = str(input('digite uma letra: '))
    letras.lower()

    if letras == 'a':
        letra1 = 'a'
    elif letras == 'm':
        letra2 = 'm'
        letra8 = 'm'
    elif letras == 'e':
        letra3 = 'e'
    elif letras == 'n':
        letra4 = 'n'
    elif letras == 'd':
        letra5 = 'd'
    elif letras == 'o':
        letra6 = 'o'
    elif letras == 'i':
        letra7 = 'i'
    else:
        tot += 1
        tot2 -= 1
        print('você errou')
        print(f'se erra mais {tot2} você perde.')

    print(letra1,letra2,letra3,letra4,letra5,letra6,letra7,letra8, end='')
    print('\n')

    palavra = letra1 + letra2 + letra3 + letra4 + letra5 + letra6 + letra7 + letra8

    if palavra == 'amendoim':
        break
    if tot > 5:
        print('você perdeu.')
        break