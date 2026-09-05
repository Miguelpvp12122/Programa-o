import time
import random

pagou = ''
def hub(id):
    tot1 = tot2 = 0
    global mana
    global HP
    global classe
    global Fugir
    global inte
    
    veneno = 0
    veneno2 = 0

    Ajuda = False
    Player = False

    defedendo = 0

    summon = False

    DF = 0
    MOT = 0

    CaraCoroa = ['Cara', 'Coroa']
    nomeI = ['Goblin']

    if id == 0:
        tipoATC = 'Atacou com seu machado'
        Fugir = True
        inimigo = 0
        inimigo += 12
        ataqueI = random.randint(4, 5)

    elif id == 1:
        tipoATC = 'Atacou com sua grande espada'
        Fugir = False
        inimigo = 0
        inimigo += 23
        ataqueI = random.randint(7, 8)
        nomeI.clear()
        nomeI.append('Cavaleiro')
    


    elif id == 2:
        tipoATC = 'Atacou com uma mordida'
        Fugir = False
        inimigo = 0
        inimigo += 6
        ataqueI = random.randint(3, 5)
        nomeI.clear()
        nomeI.append('Aranha mãe')
    
    elif id == 3:
        tipoATC = 'Atacou com uma mordida'
        Fugir = True
        inimigo = 0
        inimigo += 18
        ataqueI = random.randint(6, 8)
        nomeI.clear()
        nomeI.append('Aranha')

    elif id == 4:
        tipoATC = 'Atacou com sua grande patada'
        Fugir = False
        inimigo = 0
        inimigo += 25
        if pagou == 'N':
            inimigo -= 5
        ataqueI = random.randint(9, 10)
        nomeI.clear()
        nomeI.append('<Desconhecido>')
    
    elif id == 5:
        tipoATC = 'Atacou com uma mordida e patada'
        Fugir = False
        inimigo = 0
        inimigo += 26
        ataqueI = random.randint(10, 11)
        nomeI.clear()
        nomeI.append('MONSTRO')
    


    elif id == 6:
        tipoATC = 'Atacou com um soco'
        Fugir = True
        inimigo = 0
        inimigo += 26
        if acer == 'S':
            inimigo -= 5
        ataqueI = random.randint(9, 10)
        nomeI.clear()
        nomeI.append('Golem de pedra')
    
    elif id == 7:
        tipoATC = 'Atacou com uma chifrada'
        Fugir = False
        inimigo = 0
        inimigo += 22
        ataqueI = random.randint(10, 11)
        nomeI.clear()
        nomeI.append('Pequeno colosso')

    elif id == 8:
        tipoATC = 'Atacou com uma mordida'
        Fugir = True
        inimigo = 0
        inimigo += 20
        ataqueI = random.randint(10, 11)
        nomeI.clear()
        nomeI.append('Monstro de carne')

    elif id == 9:
        tipoATC = 'Atacou jogando acido'
        Fugir = False
        inimigo = 0
        inimigo += 25
        ataqueI = random.randint(12, 13)
        nomeI.clear()
        nomeI.append('Caminho de carne')
    

    elif id == 10:
        tipoATC = 'Atacou jogando acido'
        Fugir = False
        Ajuda = True
        inimigo = 0
        inimigo += 0
        ataqueI = random.randint(15, 16)
        nomeI.clear()
        nomeI.append('Grande serpente')
    
    elif id == 11:
        tipoATC = 'Atacou jogando acido'
        Fugir = False
        Player = True
        inimigo = 0
        inimigo += 0
        ataqueI = random.randint(16, 17)
        nomeI.clear()
        nomeI.append('Grande serpente')
    
    if matando == 5:
        Fugir = False
    
    print('==========================')
    print('         LUTEM!!!         ')
    print('==========================')
    print('\n')

    while True:
        if veneno > 0:
            veneno -= 1
            inimigo -= 1

        print('\n')
        if id == 0:
            ataqueI = random.randint(3, 4)
        elif id == 1:
            ataqueI = random.randint(7, 8)
        elif id == 2:
            ataqueI = random.randint(3, 5)
        elif id == 3:
            ataqueI = random.randint(6, 8)
        elif id == 4:
            ataqueI = random.randint(9, 10)
        elif id == 5:
            ataqueI = random.randint(10, 11)
        elif id == 6:
            ataqueI = random.randint(8, 10)
        elif id == 7:
            ataqueI = random.randint(10, 11)
        elif id == 8:
            ataqueI = random.randint(10, 11)
        elif id == 9:
            ataqueI = random.randint(12, 13)

        if DF > 0:
            ataqueI -= DF
        
        if ataqueI < 1:
            ataqueI = 1

        ataque1 = random.randint(3, 4)
        ataque2 = random.randint(7, 8)
        ataque3 = random.randint(1, 12)

        sangue = random.randint(1, 4)

        cri = ['1', '2', '3', '4']
        criI = ['1', '2', '3', '4']

        Critico = random.choice(cri)
        CriticoI = random.choice(criI)

        print('Heroi:')
        print(f' |Classe| > \033[35m{jogador[0]}\033[m')
        print(f' |HP    | > \033[32m{HP}\033[m')
        print(f' |Mana  | > \033[34m{mana}\033[m')
        print(f' |Defesa| > \033[36m{DF}\033[m')
        if Fugir == True:
            boni = '\033[31mPossivel\033[m'
        elif Fugir == False:
            boni = '\033[31mImpossivel\033[m'
        if matando == 5:
            boni = '\033[31mNão, mate\033[m'
        print(f' |Fugir | > {boni}')
        print('')
        print('')
        print('Inimigo:')
        print(f' |Nome   | > \033[35m{nomeI[0]}\033[m')
        print(f' |HP     | > \033[32m{inimigo}\033[m')
        print(f' |Dano   | > \033[31m{ataqueI}\033[m')
        print('')
        print('')
        time.sleep(2)

        print('='*40)
        print('HUB de opções:')
        print('='*40)
        print('|Atacar| [1]')
        print('|Itens | [2]')
        print('|Defesa| [3]')
        print('|Fugir | [4]')
        print('='*40)
        time.sleep(2)
        print('\n')

        while True:
            hub = str(input('Digite algumas das opções: '))
            if hub in '1234':
                break
            print('')
            print('\033[31mErro: Digite umas das opções\033[m')
            time.sleep(0.5)
            print('')
            print('')
        time.sleep(2)
        print('\n')

        if hub == '1':

            if jogador == ['Guerreiro']:
                
                ataque1 = random.randint(5, 6)
                ataque2 = random.randint(8, 10)
                ataque3 = random.randint(1, 16)
                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)

                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6


                print('=======================================')
                print('HUB de ataque:')
                print('=======================================')
                print('|Ataque rapido| = 5/6 de dano:     [1]')
                print('|Ataque pesado| = 8/10 de dano:    [2]')
                print('|Tudo ou nada!| = 1 a 16 de dano:  [3]')
                print('=======================================')
                time.sleep(2)
                print('\n')

                while True:
                    escolha = str(input('Escolha algum ataque: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                print('\n')

                if escolha == '1':
                    inimigo -= ataque1
                    print(
                        f'\033[31mO heroi corre e da uma espadada em {nomeI[0]}, -{ataque1} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    ataqueI += 1
                    time.sleep(2)
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    print(
                        f'\033[31mO heroi da um grande pulo e da uma espadada em {nomeI[0]}, -{ataque2} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    print(
                        'O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    HP -= sangue
                    print(
                        f'\033[31mTudo ou nada!!! O heroi usa de uma magia que enpunha a espada dele com seu sangue dando um grande corte em {nomeI[0]}, -{ataque3} de dano, o heroi perde sangue ele leva -{sangue}\033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    print(f'\033[31mO heroi perde sangue ele leva -{sangue} de dano {HP} de HP\033[m')
                    time.sleep(4)
                    print('\n')

            elif jogador == ['Arqueiro']:

                ataque1 = random.randint(4, 5)
                ataque2 = random.randint(7, 8)
                ataque3 = 10

                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                
                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6

                print('============================================')
                print('HUB de ataques:')
                print('============================================')
                print('|Tiros consecutivos| = 4/5 de dano:     [1]')
                print('|Tiro certeiro     | = 7/8 de dano:     [2]')
                print('|Tiro magico       | = 10 de dano:      [3]')
                print('============================================')
                time.sleep(2)
                print('\n')

                while True:
                    escolha = str(input('Escolha algum ataque: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                print('\n')

                if escolha == '1':
                    inimigo -= ataque1
                    print(
                        f'\033[31mO heroi puxa seu arco dando tiros consecutivos em {nomeI[0]}, -{ataque1} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    print(
                        f'\033[31mO heroi segura seu arco com força e da um tiro certeiro em {nomeI[0]}, -{ataque2} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    print(
                        'O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    if mana >= 20:
                        inimigo -= ataque3
                        mana -= 20
                        print(
                            f'\033[31mO heroi enche seu arco com uma magia e da um grande tiro em {nomeI[0]}, -{ataque3} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        print(
                            f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        print(f'\033[31mO heroi deu uma flechada normal em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI -= 3
                        time.sleep(2)
                        print('\n')

            elif jogador == ['Mago']:
                ataque1 = random.randint(5, 7)
                ataque2 = random.randint(8, 10)
                ataque3 = random.randint(10, 13)

                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)

                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6

                print('=========================================')
                print('HUB de ataque:')
                print('=========================================')
                print('|Em chamas!     | = 5/7 de dano:     [1]')
                print('|Absorva        | = 8/10 de dano:    [2]')
                print('|Pacto de sangue| = 10/15 de dano:   [3]')
                print('=========================================')
                time.sleep(2)
                print('\n')

                while True:
                    escolha = str(input('Escolha algum ataque: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                print('\n')

                if escolha == '1':
                    if mana >= 10:
                        inimigo -= ataque1
                        mana -= 10
                        print(
                            f'\033[31mO heroi usa chamas pra queimar {nomeI[0]}, -{ataque1} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        print(
                            f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI -= 3
                        time.sleep(2)
                        print('\n')

                elif escolha == '2':
                    if mana >= 15:
                        inimigo -= ataque2
                        mana -= 15
                        print(f'\033[31mO heroi absorve {nomeI[0]} para as sombras, -{ataque2} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        print(
                            f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI -= 3
                        time.sleep(2)
                        print('\n')

                elif escolha == '3':
                    if mana >= 25:
                        sangue -= 1
                        mana -= 20
                        HP -= sangue
                        inimigo -= ataque3
                        print(f'\033[31mO heroi faz um pacto pra fazer um grande ataque das trevas em {nomeI[0]} usando do seu sangue e mana, -{ataque3} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        print(
                            f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        print(
                            f'O heroi perde sangue ele leva -{sangue} de dano {HP} de HP')
                        time.sleep(4)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        print('')
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(3)
                        print('\n')



            elif jogador == ['Assasino']:

                if veneno > 0:
                    print('\033[31m!!!')
                    print(f'O veneno faz efeito em {nomeI[0]} dando 1 de dano\033[m')
                    print('')
                    print('')
                    time.sleep(3)

                ataque1 = 7
                ataque2 = 9
                ataque3 = 13
                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)

                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6


                print('=====================================')
                print('HUB de ataque:')
                print('=====================================')
                print('|Ataque furtivo| = 7 de dano:    [1]')
                print('|Facada rapida | = 9 de dano:    [2]')
                print('|Envenenamento | = 13 de dano:   [3]')
                print('=====================================')
                time.sleep(2)
                print('\n')

                while True:
                    escolha = str(input('Escolha algum ataque: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                print('\n')

                if escolha == '1':
                    inimigo -= ataque1
                    print(f'\033[31mO heroi some e logo da uma facada nas costa de {nomeI[0]}, -{ataque1} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    veneno += 1
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    print(f'\033[31mO heroi da um grande avanço em {nomeI[0]} dando uma facada, -{ataque2} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    print('O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 1
                    veneno += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    print(f'\033[31mO heroi usa um bolsa de veneno jogando em {nomeI[0]}, -{ataque3} de dano\033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    print('O veneno é muito forte deixa o heroi envenenado')
                    veneno += 3
                    veneno2 += 2
                    time.sleep(4)
                    print('\n')
            
            elif jogador == ['Bárbaro']:

                ataque1 = random.randint(6, 7)
                ataque2 = random.randint(9, 11)
                ataque3 = random.randint(14, 16)
                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)

                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6


                print('==========================================')
                print('HUB de ataque:')
                print('==========================================')
                print('|Jogar machado   | = 6/7 de dano:     [1]')
                print('|Pulo bárbaro!   | = 9/11 de dano:    [2]')
                print('|Combo de machado| = 14/16 de dano:   [3]')
                print('==========================================')
                time.sleep(2)
                print('\n')

                while True:
                    escolha = str(input('Escolha algum ataque: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                print('\n')

                if escolha == '1':
                    inimigo -= ataque1
                    print(f'\033[31mO heroi joga o machado em {nomeI[0]} voltando pra sua mão, -{ataque1} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    ataqueI += 2
                    time.sleep(3)
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    print(f'\033[31mO heroi da um grande pulo dando uma machada em {nomeI[0]}, -{ataque2} de dano \033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    ataqueI += 3
                    time.sleep(3)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    ataqueI += 4
                    print(f'\033[31mO heroi da um combo em {nomeI[0]} finalizando com um estrondo, -{ataque3} de dano\033[m')
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(3)
                    print('\n')

            if jogador == ['Chance']:
                
                ataque1 = random.randint(4, 5)
                ataque2 = random.randint(8, 9)
                ataque3 = random.randint(9, 11)
                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)

                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6


                while True:
                    print('======================================')
                    print('HUB de ataque:')
                    print('======================================')
                    print('|Pulo cortante| = 4/5 de dano:   [1]')
                    print('|Tsume kiri   | = 8/9 de dano:   [2]')
                    print('|Lua de sangue| = 9/11 de dano:  [3]')
                    print('|Cara ou coroa| = Passiva:       [4]')
                    print('======================================')
                    time.sleep(2)
                    print('\n')

                    while True:
                        escolha = str(input('Escolha algum ataque: '))
                        if escolha in '1234':
                            break
                        print('')
                        print('\033[31mErro: Digite umas das opções\033[m')
                        time.sleep(0.5)
                        print('')
                        print('')
                    print('\n')

                    if escolha == '1':
                        inimigo -= ataque1
                        print(f'\033[31mO heroi da um pulo dando um corte em {nomeI[0]}, -{ataque1} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 1
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '2':
                        inimigo -= ataque2
                        print(f'\033[31mO heroi da uma espadada pra baixo e logo dando um perfuro em {nomeI[0]}, -{ataque2} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 2
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '3':
                        inimigo -= ataque3
                        print(f'\033[31mO heroi da um corte como lua de sangue em {nomeI[0]}, -{ataque3} de dano\033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(4)
                        print('\n')
                        break
                    
                    elif escolha == '4':
                        print('O espirito apareceu')
                        time.sleep(1)
                        print('Se for coroa ataque aumenta')
                        time.sleep(1)
                        print('Se for cara perde o turno')
                        time.sleep(1)
                        print('')
                        print('O espirito joga a moeda e caiu...')
                        time.sleep(3)
                        CACO = random.choice(CaraCoroa)

                        if CACO == 'Coroa':
                            print('Espirito: Coroa, seus ataques ficou mais forte')
                            time.sleep(2)
                            print('+ 4 de dano pra todos os ataques')
                            time.sleep(3)
                            ataque1 += 4
                            ataque2 += 4
                            ataque3 += 4
                            print('\n')
                            print('\n')
                        elif CACO == 'Cara':
                            print('Espirito: Cara, você perdeu seu turno')
                            time.sleep(2)
                            print('\n')
                            break
            
            elif jogador == ['Summoner']:

                ataque1 = random.randint(5, 6)
                ataque2 = random.randint(8, 9)
                ataque3 = 15

                if Critico in '3':
                    ataque1 += 1
                    ataque2 += 2
                    ataque3 += 3
                    print('='*40)
                    print('Proximo ataque será critico!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                
                if Nivel > 0:
                    print('='*40)
                    print('Ataque aumentado por causa do seu nivel!')
                    print('='*40)
                    print('')
                    print('')
                    time.sleep(2)
                    if Nivel == 1:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 1
                    elif Nivel == 2:
                        ataque1 += 1
                        ataque2 += 1
                        ataque3 += 2
                    elif Nivel == 3:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 2
                    elif Nivel == 4:
                        ataque1 += 2
                        ataque2 += 2
                        ataque3 += 3
                    elif Nivel == 5:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 3
                    elif Nivel == 6:
                        ataque1 += 3
                        ataque2 += 3
                        ataque3 += 4
                    elif Nivel == 7:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 4
                    elif Nivel == 8:
                        ataque1 += 4
                        ataque2 += 4
                        ataque3 += 5
                    elif Nivel == 9:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 5
                    elif Nivel == 10:
                        ataque1 += 5
                        ataque2 += 5
                        ataque3 += 6

                while True:
                    print('=============================================')
                    print('HUB de ataques:')
                    print('=============================================')
                    print('|Cortes consecutivos| = 5/6 de dano:     [1]')
                    print('|Facada unica       | = 8/9 de dano:     [2]')
                    print('|Liberação maxima   | = 15 de dano:      [3]')
                    print('|Ativar summon      | = Passiva:         [4]')
                    print('=============================================')
                    time.sleep(2)
                    print('\n')

                    while True:
                        escolha = str(input('Escolha algum ataque: '))
                        if escolha in '1234':
                            break
                        print('')
                        print('\033[31mErro: Digite umas das opções\033[m')
                        time.sleep(0.5)
                        print('')
                        print('')
                    print('\n')

                    if escolha == '1':
                        inimigo -= ataque1
                        print(f'\033[31mO heroi puxa suas adagas dando cortes sem parar em {nomeI[0]}, -{ataque1} de dano \033[m')

                        if summon == True:
                            print(f'O summon deu um soco em {nomeI[0]}')
                            time.sleep(2)
                            ataqueI -= 1
                            inimigo -= 4

                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 1
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '2':
                        inimigo -= ataque2
                        print(f'\033[31mO heroi da um avanço em {nomeI[0]} e da uma facada unica, -{ataque2} de dano \033[m')

                        if summon == True:
                            print(f'O summon deu um soco em {nomeI[0]}')
                            time.sleep(2)
                            ataqueI -= 2
                            inimigo -= 4

                        print('')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 2
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '3':
                        if summon == True:
                            inimigo -= ataque3
                            print(f'\033[31mO summon libera todo seu poder dando um soco em {nomeI[0]}, -{ataque3} de dano \033[m')
                            time.sleep(2)
                            print('O summon morreu')
                            summon = False
                            print(f'{nomeI[0]} Está com {inimigo} de HP')
                            time.sleep(2)
                            print('\n')
                            break
                        elif summon == False:
                            print('Ative o summon pra usar esse ataque')
                            time.sleep(2)
                            print('\n')
        
                    
                    elif escolha == '4':
                        if summon == False:
                            print('O summon nasceu das sombras')
                            time.sleep(2)
                            HP -= 5
                            print('O heroi usou do sangue pra ativar ele')
                            print(f'\033[31mO HP está {HP}\033[m')
                            time.sleep(2)
                            summon = True
                            print('\n')

                        elif summon == True:
                            print('O summon já está ativado')
                            print('\n')

                    

        if hub == '2':
            print('='*40)
            print('HUB de itens: ')
            print('='*40)
            print('Bolsa de intens:')
            for n in intens:
                tot1 += 1
                print(f'|{n}|            [{tot1}]')
            print('='*40)
            tot1 -= 4
            time.sleep
            print('\n')

            while True:
                    escolha = str(input('Escolha algum item: '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')

            if escolha == '1':
                if intens[0] == 'Poção pequena':
                    HP += 6
                    print(
                        f'\033[32mO heroi tomou uma poção pequena de vida, o HP está {HP}\033[m')
                    del intens[0]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[0]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[0]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção de mana':
                    mana += 150
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[0]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == '             ':
                    print(f'Nenhum intem encontrado')
                    time.sleep(2)
                    print('\n')

            elif escolha == '2':
                if intens[1] == 'Poção pequena':
                    HP += 6
                    print(
                        f'\033[32mO heroi tomou uma poção pequena de vida, o HP está {HP}\033[m')
                    del intens[1]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[1]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[1]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção de mana':
                    mana += 150
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[1]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == '             ':
                    print(f'Nenhum intem encontrado')
                    time.sleep(2)
                    print('\n')

            elif escolha == '3':
                if intens[2] == 'Poção pequena':
                    HP += 6
                    print(
                        f'\033[32mO heroi tomou uma poção pequena de vida, o HP está {HP}\033[m')
                    del intens[2]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[2]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[2]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção de mana':
                    mana += 150
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[2]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == '             ':
                    print(f'Nenhum intem encontrado')
                    time.sleep(2)
                    print('\n')

            if escolha == '4':
                if intens[3] == 'Poção pequena':
                    HP += 6
                    print(
                        f'\033[32mO heroi tomou uma poção pequena de vida, o HP está {HP}\033[m')
                    del intens[3]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[3]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[3]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção de mana':
                    mana += 150
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[3]
                    intens.append('             ')
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == '             ':
                    print(f'Nenhum intem encontrado')
                    time.sleep(2)
                    print('\n')

        elif hub == '3':
            if jogador == ['Guerreiro']:
                defesa = 'seu escudo'
                defedendo = random.randint(2, 4)
            elif jogador == ['Arqueiro']:
                defesa = 'seu arco'
                defedendo = random.randint(2, 3)
            elif jogador == ['Mago']:
                defesa = 'sua magia'
                defedendo = random.randint(2, 3)
            elif jogador == ['Assasino']:
                defesa = 'sua adaga'
                defedendo = random.randint(2, 3)
            elif jogador == ['Bárbaro']:
                defesa = 'seu machado'
                defedendo = random.randint(2, 4)
            elif jogador == ['Chance']:
                defesa = 'sua espada'
                defedendo = random.randint(2, 3)
            elif jogador == ['Summoner']:
                defesa = 'suas adagas'
                defedendo = random.randint(2, 3)

            DF += defedendo

            ataqueI -= DF

            if ataqueI < 1:
                ataqueI = 1

            print(f'O heroi defende com {defesa}')
            time.sleep(1)
            print(f'O ataque do inimigo foi reduzido a {defedendo}')
            time.sleep(2)
            print('')
            print(f'O ataque do inimigo no maximo pode ser {ataqueI}')
            time.sleep(3)
            print('\n')

        elif hub == '4':
            if Fugir == True:
                print('O heroi conseguiu fugir do inimigo')
                time.sleep(2)
                Fugir = 'A'
                break
            elif Fugir == False:
                print('O heroi tenta corre mais não consegue!')
                time.sleep(2)
                print(f'\033[37m{nomeI[0]} Bloqueia o caminho\033[m')
                time.sleep(2)
            time.sleep(1)
            print('\n')

        if inimigo <= 0:
            time.sleep(1)
            break

        if Ajuda == True:
            if inimigo <= 25:
                time.sleep(2)
                break
        
        if Player == True:
            print('')
            print('')
            print('A elfa deu um tiro na serpente')
            time.sleep(2)
            inimigo -= 8
            print(f'8 De dano, a sepente está com {inimigo}')
            time.sleep(2)
            print('')
            print('')
        
        print(f'Hora de {nomeI[0]} atacar!')

        if CriticoI in '3':
            ataqueI += 2
            print(f'O ataque do {nomeI[0]} será critico!')
            print('')
            time.sleep(2)

        HP -= ataqueI
        print(f'\033[31m{nomeI[0]} {tipoATC}, -{ataqueI}\033[m')
        time.sleep(2)
        print(f'O heroi está com {HP} de HP')
        time.sleep(3)
        print('\n')

        if veneno2 > 0:
            print('!!!')
            print('O veneno fez efeito no heroi')
            HP -= 1
            veneno2 -= 1

        if HP <= 0:
            if MOT == 0:
                HP = 1
                print('')
                print('Apesar do ataque o heroi continua vivo com apenas')
                print('\033[31m1 De HP\033[m')
                time.sleep(1)
                print('')
                print('')
                MOT += 1

        if HP <= 0:
            print('\033[31mO heroi morreu...\033[m')
            time.sleep(2)
            print(f'Continue {nome}!')
            time.sleep(1)
            print('\n')
            print('\n')
            break





def nivel():
    global Nivel
    if Nivel == 0:
        if XP >= 150:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 32 pontos')
            time.sleep(2)
            print('A mana está com 60 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')

    if Nivel == 1:
        if XP >= 320:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 33 pontos')
            time.sleep(2)
            print('A mana está com 70 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')
    
    if Nivel == 2:
        if XP >= 420:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 35 pontos')
            time.sleep(2)
            print('A mana está com 80 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')

    if Nivel == 3:
        if XP >= 520:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 37 pontos')
            time.sleep(2)
            print('A mana está com 90 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')

    if Nivel == 4:
        if XP >= 620:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 40 pontos')
            time.sleep(2)
            print('A mana está com 100 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')

    if Nivel == 5:
        if XP >= 720:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 40 pontos')
            time.sleep(2)
            print('A mana está com 100 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')  

    if Nivel == 6:
        if XP >= 820:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 40 pontos')
            time.sleep(2)
            print('A mana está com 100 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')  

    if Nivel == 7:
        if XP >= 720:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 45 pontos')
            time.sleep(2)
            print('A mana está com 110 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')  

    if Nivel == 8:
        if XP >= 720:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 45 pontos')
            time.sleep(2)
            print('A mana está com 110 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')

    if Nivel == 9:
        if XP >= 720:
            print(f'O heroi subiu de nivel!')
            time.sleep(1)
            Nivel += 1
            print(f'\033[35mO nivel está {Nivel}\033[m')
            time.sleep(2)
            print('O HP está com 45 pontos')
            time.sleep(2)
            print('A mana está com 120 pontos')
            time.sleep(2)
            print('O ataque aumentou')
            time.sleep(2)
            print('\n')  






























































HP = 1
mana = 50
Dori = 55


XP = 0
Nivel = 10
NivelB  = 10


Morte = 0
Mortes = 0
Vivo = ''

Fugir = False

ACABAR = 0
cutcine = 0
Raiva = 0

classe = ['Guerreiro', 'Arqueiro', 'Mago']
intens = ['Poção pequena', 'Poção pequena', 'Poção pequena']
bau = ['cobra', 'dori', 'Poção pequena', 'nada']

nome = 'Miguel'

jogador = ['Chance']



































NivelB = 10
Nivel = 10
matando = 5
XPB = 1000
intensB = intens[:]












Dori2 = 100
acer = 0
























print('Obrigado por ter jogado!')
time.sleep(2)
print('')

print('Agradecimento aos meus amigos')
time.sleep(3)
print('Eles me ajudarão com o jogo')
time.sleep(2)
print('')

print('Agradecimento especial ao meu pai')
time.sleep(2)
print('Esse jogo nunca iria existi sem ele')
time.sleep(3)
print('')

print('Agora eu Miguel vou estudar mais ainda')
time.sleep(2)
print('Pra ter um jogo de verdade!')
time.sleep(2)
print('')


print('Jogo criado por: Miguel Coutinho Simões')
time.sleep(3)
print('')
if matando == 5:
    print('Você fez o final Geno')
    time.sleep(2)
    print('Undertale reference KKKKKK')
    time.sleep(2)

print('\n')
print('Assim eu tinha falado sobre um boss bonus')
time.sleep(2)
print('Vou fazer não KKKKKKKKKKKKKKKKKKKKKKKKK')
time.sleep(2)
print('Ou sim sei la')
