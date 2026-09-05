import random

nome = input('qual seu nome? ')
print(f'então vamos o pedra papel e tesoura {nome}')
print('\n')

pessoa = input('qual escolhe (pedra papel ou tesoura)? ')

placar = int(0)
plabo = int(0)

robo = ['pedra', 'papel', 'tesoura']
rodada = random.choice(robo)
rodada2 = random.choice(robo)
rodada3 = random.choice(robo)
rodada4 = random.choice(robo)
rodada5 = random.choice(robo)

if pessoa == 'pedra' and rodada == 'pedra':
    placar += 1
    plabo += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print('voi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa == 'pedra' and rodada == 'tesoura':
    print(f'você botou {pessoa} e o robo botou {rodada}')
    placar += 1
    print(f'o placar está {nome}:{placar} e robo:{plabo}')
elif pessoa == 'tesoura' and rodada == 'pedra':
    print(f'você botou {pessoa} e o robo botou {rodada}')
    plabo += 1
    print(f'o placar está {nome}:{placar} e o robo:{plabo} ')

elif pessoa == 'pedra' and rodada == 'papel':
    plabo += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa == 'papel' and rodada == 'pedra':
    placar += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa == 'papel' and rodada == 'papel':
    placar += 1
    plabo += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print('foi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}.')

elif pessoa == 'papel' and rodada == 'tesoura':
    plabo += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa == 'tesoura' and rodada == 'papel':
    placar += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa == 'tesoura' and rodada == 'tesoura':
    placar += 1
    print(f'você botou {pessoa} e o robo botou {rodada}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
print('\n')

print('segunda rodada: ')
pessoa2 = input('qual escolhe? ')

if pessoa2 == 'pedra' and rodada2 == 'pedra':
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    placar += 1
    plabo += 1
    print('voi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa2 == 'pedra' and rodada2 == 'tesoura':
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    placar += 1
    print(f'o placar está {nome}:{placar} e robo:{plabo}')
elif pessoa2 == 'tesoura' and rodada2 == 'pedra':
    plabo += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo} ')

elif pessoa2 == 'pedra' and rodada2 == 'papel':
    plabo += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa2 == 'papel' and rodada2 == 'pedra':
    placar += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa2 == 'papel' and rodada2 == 'papel':
    placar += 1
    plabo += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print('foi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}.')

elif pessoa2 == 'papel' and rodada2 == 'tesoura':
    plabo += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa2 == 'tesoura' and rodada2 == 'papel':
    placar += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa2 == 'tesoura' and rodada2 == 'tesoura':
    placar += 1
    print(f'você botou {pessoa2} e o robo botou {rodada2}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
print('\n')

pessoa3 = input('qual escolhe? ')

if pessoa3 == 'pedra' and rodada3 == 'pedra':
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    placar += 1
    plabo += 1
    print('voi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa3 == 'pedra' and rodada3 == 'tesoura':
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    placar += 1
    print(f'o placar está {nome}:{placar} e robo:{plabo}')
elif pessoa3 == 'tesoura' and rodada3 == 'pedra':
    plabo += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo} ')

elif pessoa3 == 'pedra' and rodada3 == 'papel':
    plabo += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa3 == 'papel' and rodada3 == 'pedra':
    placar += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa3 == 'papel' and rodada3 == 'papel':
    placar += 1
    plabo += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print('foi enpate.')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}.')

elif pessoa3 == 'papel' and rodada3 == 'tesoura':
    plabo += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
elif pessoa3 == 'tesoura' and rodada3 == 'papel':
    placar += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')

elif pessoa3 == 'tesoura' and rodada3 == 'tesoura':
    placar += 1
    print(f'você botou {pessoa3} e o robo botou {rodada3}')
    print(f'o placar está {nome}:{placar} e o robo:{plabo}')
print('\n')


if placar == 3:
    print(f'{nome} GANHOU!!!')
elif plabo == 3:
    print('robo GANHOU!!!')
elif placar == 1 or placar == 2:
    print('nimquem ganhou ainda! Vamos fazer mais 1')
    pessoa4 = input('qual escolhe? ')
    if pessoa4 == 'pedra' and rodada4 == 'pedra':
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        placar += 1
        plabo += 1
        print('voi enpate.')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')

    elif pessoa4 == 'pedra' and rodada4 == 'tesoura':
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        placar += 1
        print(f'o placar está {nome}:{placar} e robo:{plabo}')
    elif pessoa4 == 'tesoura' and rodada4 == 'pedra':
        plabo += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo} ')

    elif pessoa4 == 'pedra' and rodada4 == 'papel':
        plabo += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')
    elif pessoa4 == 'papel' and rodada4 == 'pedra':
        placar += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')

    elif pessoa4 == 'papel' and rodada4 == 'papel':
        placar += 1
        plabo += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print('foi enpate.')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}.')

    elif pessoa4 == 'papel' and rodada4 == 'tesoura':
        plabo += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')
    elif pessoa4 == 'tesoura' and rodada4 == 'papel':
        placar += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')

    elif pessoa4 == 'tesoura' and rodada4 == 'tesoura':
        placar += 1
        print(f'você botou {pessoa4} e o robo botou {rodada4}')
        print(f'o placar está {nome}:{placar} e o robo:{plabo}')
    print('\n')
    if placar == 3:
        print(f'{nome} GANHOU!!!')
    elif plabo == 3:
        print('robo GANHOU!!!')
    elif placar == 1 or placar == 2:
        print('nimquem ganhou ainda! Vamos fazer mais 1')
        pessoa5 = input('ULTIMA RODADA qual escolhe? ')
        if pessoa5 == 'pedra' and rodada5 == 'pedra':
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            placar += 1
            plabo += 1
            print('voi enpate.')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')

        elif pessoa5 == 'pedra' and rodada5 == 'tesoura':
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            placar += 1
            print(f'o placar está {nome}:{placar} e robo:{plabo}')
        elif pessoa5 == 'tesoura' and rodada5 == 'pedra':
            plabo += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo} ')

        elif pessoa5 == 'pedra' and rodada5 == 'papel':
            plabo += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')
        elif pessoa5 == 'papel' and rodada5 == 'pedra':
            placar += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')

        elif pessoa5 == 'papel' and rodada5 == 'papel':
            placar += 1
            plabo += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print('foi enpate.')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}.')

        elif pessoa5 == 'papel' and rodada5 == 'tesoura':
            plabo += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')
        elif pessoa5 == 'tesoura' and rodada5 == 'papel':
            placar += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')

        elif pessoa5 == 'tesoura' and rodada5 == 'tesoura':
            placar += 1
            print(f'você botou {pessoa5} e o robo botou {rodada5}')
            print(f'o placar está {nome}:{placar} e o robo:{plabo}')
            print('\n')
            if placar == 3:
                print(f'{nome} GANHOU!!!')
            elif plabo == 3:
                print('robo GANHOU!!!')
        