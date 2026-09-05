import random

rodar_dado = random.randint(1, 6)
rodar_dado2 = random.randint(1, 6)
rodar_dado3 = random.randint(1, 6)
rodar_dado4 = random.randint(1, 6)
rodar_dado5 = random.randint(1, 6)
rodar_dado6 = random.randint(1, 6)

hp = (30) 

batalha1 = (input('se quiser atacar bote 1, se quise ir escondido bota 2: '))

if batalha1 == '1':
    print('você começou uma luta! ')
    atacar = input('aperte ENTER pra rodar o dado: ')
    print(f'{atacar}')
    if atacar == '':
        soma = (rodar_dado+rodar_dado2)
        print(f'ficou:{soma} ')
        if soma >6:
            print('voce ganhou e passou pra um novo quarto')
        else:
            print('você atacou mais nao foi o sufuciente pra matar o inimigo')
            print('agora é a fez do orc atacar: ')
            ataque = (rodar_dado5+rodar_dado6)
            inimigo = (ataque - hp)
            print(f'a ataque do inimigo foi {inimigo} seu hp esta {hp}')
            atacar2 = input('aperte ENTER pra rodar dado: ')
            total = (5-soma)
            soma2 = (rodar_dado3+rodar_dado4)
            if soma2 >total:
                print('você ganhou e passou pra um novo quarto')