import time
import random

matando = 0

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
        ataqueI = 5

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
        tipoATC = 'Atacou com um bote'
        Fugir = False
        Ajuda = True
        inimigo = 0
        inimigo += 50
        ataqueI = random.randint(14, 15)
        nomeI.clear()
        nomeI.append('Grande serpente')
    
    elif id == 11:
        tipoATC = 'Atacou com um bote'
        Fugir = False
        Player = True
        inimigo = 0
        inimigo += 45
        ataqueI = random.randint(14, 16)
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
            ataqueI = 5
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
        elif id == 10:
            ataqueI = random.randint(14, 15)
        elif id == 11:
            ataqueI = random.randint(14, 16)

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
                    print('O ataque será critico!')
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
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi corre e da uma espadada em {nomeI[0]}, -{ataque1} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    ataqueI += 1
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi da um pulo e da um corte em {nomeI[0]}, -{ataque2} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    if inimigo < 0:
                        inimigo = 0
                    HP -= sangue
                    print(f'\033[31mO heroi usa uma magia em sua espada dando um corte em {nomeI[0]}, -{ataque3} de dano\033[m')
                    time.sleep(3)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print(f'\033[31mO heroi perde sangue ele leva -{sangue} de dano {HP} de HP\033[m')
                    time.sleep(2)
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
                    print('O aumentado por causa do seu nivel!')
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
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi puxa seu arco dando tiros consecutivos em {nomeI[0]}, -{ataque1} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    print(f'\033[31mO heroi segura seu arco com força e da um tiro certeiro em {nomeI[0]}, -{ataque2} de dano \033[m')
                    time.sleep(3)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    if mana >= 20:
                        inimigo -= ataque3
                        if inimigo < 0:
                            inimigo = 0
                        mana -= 20
                        print(f'\033[31mO heroi enche seu arco com magia e da um tiro em {nomeI[0]}, -{ataque3} de dano \033[m')
                        time.sleep(3)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
                        print(f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        time.sleep(2)
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi deu uma flechada normal em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        time.sleep(2)
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
                    print('O ataque será critico!')
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
                        if inimigo < 0:
                            inimigo = 0
                        mana -= 10
                        print(f'\033[31mO heroi usa chamas pra queimar {nomeI[0]}, -{ataque1} de dano \033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
                        print(f'\033[34mO heroi usou magia! Menos 10 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        print('')
                        time.sleep(2)
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI -= 3
                        time.sleep(2)
                        print('\n')

                elif escolha == '2':
                    if mana >= 15:
                        inimigo -= ataque2
                        if inimigo < 0:
                            inimigo = 0
                        mana -= 15
                        print(f'\033[31mO heroi absorve {nomeI[0]} para as sombras, -{ataque2} de dano \033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
                        print(f'\033[34mO heroi usou magia! Menos 15 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        time.sleep(2)
                        ataqueSM = random.randint(4, 6)
                        inimigo -= ataqueSM
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        time.sleep(2)
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
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi faz um pacto das trevas em {nomeI[0]}, -{ataque3} de dano \033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
                        print(f'\033[34mO heroi usou magia! Menos 20 de mana, a mana está {mana}\033[m')
                        time.sleep(2)
                        print(f'O heroi perde sangue ele leva -{sangue} de dano {HP} de HP')
                        time.sleep(2)
                        print('\n')
                    else:
                        print('\033[36mO heroi não tem mana o suficiente pra executar o ataque\033[m')
                        time.sleep(2)
                        print('')
                        ataqueSM = random.randint(4, 6)
                        if inimigo < 0:
                            inimigo = 0
                        inimigo -= ataqueSM
                        print(f'\033[31mO heroi deu uma cajadada em {nomeI[0]}, dando -{ataqueSM} de dano\033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
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
                    print('O ataque será critico!')
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
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi some e logo da uma facada nas costa de {nomeI[0]}, -{ataque1} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    veneno += 1
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi da um grande avanço em {nomeI[0]} dando uma facada, -{ataque2} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('O ataque feito deixa o heroi vulneravel a um ataque mais forte')
                    ataqueI += 1
                    veneno += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi usa um bolsa de veneno jogando em {nomeI[0]}, -{ataque3} de dano\033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    print('O veneno é muito forte deixa o heroi envenenado')
                    veneno += 3
                    veneno2 += 2
                    time.sleep(2)
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
                    print('O ataque será critico!')
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
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi joga o machado em {nomeI[0]} voltando pra sua mão, -{ataque1} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
                    ataqueI += 2
                    time.sleep(2)
                    print('\n')

                elif escolha == '2':
                    inimigo -= ataque2
                    if inimigo < 0:
                        inimigo = 0
                    print(f'\033[31mO heroi da um grande pulo dando uma machada em {nomeI[0]}, -{ataque2} de dano \033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    ataqueI += 3
                    time.sleep(2)
                    print('\n')

                elif escolha == '3':
                    inimigo -= ataque3
                    if inimigo < 0:
                        inimigo = 0
                    ataqueI += 4
                    print(f'\033[31mO heroi da um combo em {nomeI[0]} finalizando com um estrondo, -{ataque3} de dano\033[m')
                    time.sleep(2)
                    print(f'{nomeI[0]} Está com {inimigo} de HP')
                    time.sleep(2)
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
                    print('O ataque será critico!')
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
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi da um pulo dando um corte em {nomeI[0]}, -{ataque1} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 1
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '2':
                        inimigo -= ataque2
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi da uma espadada pra baixo e logo dando um perfuro em {nomeI[0]}, -{ataque2} de dano \033[m')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 2
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '3':
                        inimigo -= ataque3
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi da um corte como lua de sangue em {nomeI[0]}, -{ataque3} de dano\033[m')
                        time.sleep(2)
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        time.sleep(2)
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
                    print('O ataque será critico!')
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
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi puxa suas adagas dando cortes sem parar em {nomeI[0]}, -{ataque1} de dano \033[m')
                        time.sleep(2)

                        if summon == True:
                            print(f'O summon deu um soco em {nomeI[0]}')
                            time.sleep(2)
                            ataqueI -= 1
                            inimigo -= 4
                            if inimigo < 0:
                                inimigo = 0

                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 1
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '2':
                        inimigo -= ataque2
                        if inimigo < 0:
                            inimigo = 0
                        print(f'\033[31mO heroi da um avanço em {nomeI[0]} e da uma facada unica, -{ataque2} de dano \033[m')
                        time.sleep(2)

                        if summon == True:
                            print(f'O summon deu um soco em {nomeI[0]}')
                            time.sleep(2)
                            ataqueI -= 2
                            inimigo -= 4
                            if inimigo < 0:
                                inimigo = 0

                        print('')
                        print(f'{nomeI[0]} Está com {inimigo} de HP')
                        ataqueI += 2
                        time.sleep(2)
                        print('\n')
                        break

                    elif escolha == '3':
                        if summon == True:
                            inimigo -= ataque3
                            if inimigo < 0:
                                inimigo = 0
                            print(f'\033[31mO summon libera todo seu poder dando um soco em {nomeI[0]}, -{ataque3} de dano \033[m')
                            time.sleep(3)
                            print('O summon morreu')
                            time.sleep(1)
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
                            time.sleep(1)
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
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[0]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[0]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[0] == 'Poção de mana':
                    mana += 40
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
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[1]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[1]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[1] == 'Poção de mana':
                    mana += 40
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[1]
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
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[2]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[2]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[2] == 'Poção de mana':
                    mana += 40
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[2]
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
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção media  ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção media de vida, o HP está {HP}\033[m')
                    del intens[3]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção grande ':
                    HP += 10
                    print(
                        f'\033[32mO heroi tomou uma poção grande de vida, o HP está {HP}\033[m')
                    del intens[3]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == 'Poção de mana':
                    mana += 40
                    print(
                        f'\033[34mO heroi tomou poção de mana, sua mana está {mana}\033[m')
                    del intens[3]
                    ataqueI -= 3
                    time.sleep(2)
                    print('\n')
                elif intens[3] == '             ':
                    print(f'Nenhum intem encontrado')
                    time.sleep(2)
                    print('\n')
            
            ataqueI = 2

        elif hub == '3':
            defedendo = 0
            if jogador == ['Guerreiro']:
                defesa = 'seu escudo'
                defedendo = random.randint(2, 4)
            elif jogador == ['Arqueiro']:
                defesa = 'seu arco'
                defedendo = random.randint(2, 3)
            elif jogador == ['Mago']:
                defesa = 'seu cajado'
                time.sleep(2)
                print('')
                print('\033[34mGanhou mais mana!\033[m')
                mana += 10
                time.sleep(2)
                print('')

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
            print(f'A defesa do heroi aumentou')
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
                if matando < 5:
                    print('O heroi tenta corre mais não consegue!')
                    time.sleep(2)
                    print(f'\033[37m{nomeI[0]} Bloqueia o caminho\033[m')
                    time.sleep(2)
                elif matando == 5:
                    print('Mate, mate, MATE!')
                    time.sleep(2)
            time.sleep(1)
            print('\n')

        if Player == True:
            print('')
            print('')
            print('\033[31mA elfa deu um tiro na serpente\033[m')
            time.sleep(2)
            inimigo -= 8
            print(f'8 De dano, a sepente está com {inimigo}')
            time.sleep(2)
            print('')
            print('\n')


        if inimigo <= 0:
            time.sleep(2)
            break

        if Ajuda == True:
            if inimigo <= 25:
                time.sleep(2)
                break
        
        print(f'Hora de {nomeI[0]} atacar!')

        if CriticoI in '3':
            ataqueI += 2
            print(f'O ataque do {nomeI[0]} será critico!')
            print('')
            time.sleep(2)

        HP -= ataqueI
        if HP < 0:
            HP = 0
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
        if XP >= 920:
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
        if XP >= 1020:
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
        if XP >= 1120:
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
              
            
            
            
































HP = 30
mana = 50
Dori = 0

inte = 0

XP = 0
Nivel = 0
NivelB = 0


Morte = 0
Mortes = 0
Vivo = ''

Fugir = False

ACABAR = 0
cutcine = 0
Raiva = 0

classe = ['Guerreiro', 'Arqueiro', 'Mago']

intens = ['Poção pequena']
intensB = ['Poção pequena']

bau = ['cobra', 'dori', 'Poção pequena', 'nada']

id = 0



print('======================')
print(' Seja bem vindo ao...')
print('======================')
print('')
time.sleep(1)
print('<~~~~~~~~~~~~~~~~~~~~~>')
time.sleep(0.3)
print('  Dark Of Mountain!!!')
time.sleep(0.3)
print('<~~~~~~~~~~~~~~~~~~~~~>')
time.sleep(0.5)
print('\n')

while True:
    escolha1 = str(input('Você deseja ver o começo da historia do jogo? [S/N]: ')).upper()[0]
    if escolha1 in ('SN'):
        break
    print('')
    print('\033[31mERRO: Escolha entre S ou N\033[m')
    time.sleep(0.5)
    print('')
    print('')

if escolha1 == 'S':
    print('')
    print('=================================================')
    print('Era tudo normal, um mundo em paz')
    time.sleep(2)
    print('Sem guerras, só armonia')
    time.sleep(1)
    print('Mais uma dia isso tudo mundou...')
    time.sleep(2)
    print('=================================================')
    print('Um mago na parte das trevas')
    print('Fez uma magia onde que o mundo foi engolido pela')
    time.sleep(3)
    print('Escuridão...')
    time.sleep(0.5)
    print('=================================================')
    print('O mago se escondeu ao topo de uma montanha')
    time.sleep(2)
    print('E você acabara com isso tudo')
    time.sleep(1)
    print('Lutando e ganhando do mago')
    time.sleep(1.5)
    print('=================================================')
    print('\n')

else:
    print('')
    print('=============')
    print('   -Certo-')
    print('=============')
    time.sleep(1.5)
    print('\n')

print('━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━')
nome = str(input('Qual o seu nome? ')).capitalize()
print('━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━')

if nome == 'Miguelpvp12122':
    print('Por favor outro nome.')
    print('Nome de um desenvolvedor não pode ser usado')
    time.sleep(1)
    print('\n')
    while True:
        nome = str(input('Digite o seu nome novamente: ')).capitalize()
        if nome == 'Miguelpvp12122':
            print('')
            print('\033[31mErro: digite outro nome\033[m')
            time.sleep(0.5)
            print('')
            print('')
            time.sleep(1)
        else:
            break

if nome == 'Henrique' or nome == 'Gabryel' or nome == 'Ruan' or nome == 'José' or nome == 'Edson' or nome == 'Ezequiel':
    print('')
    print('Já vi esse nome em algum lugar...')
    time.sleep(2)
    print('Não quero dizer')
    time.sleep(2)
    print('\n')


time.sleep(1)
print('\n')

print('━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━')
print(f'{nome}, que nome exelente.')
print('━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━')
time.sleep(2)
print('\n')

print('Escolha umas das classes pra ser a principal: ')

time.sleep(2)
print('')
print('\033[31m======================================================')
print('OBS: Será possivel trocar de classe depois da escolha ')
print('======================================================\033[m')
time.sleep(2)
print('')

print('Guerreiro [1]')
print('|Ataque rapido| = 5/6 de dano')
print('|Ataque pesado| = 8/10 de dano')
print('|Tudo ou nada!| = 1 a 16 de dano')
print('*   Não usa magia')
time.sleep(1)
print('')
print('')
print('Arqueiro  [2]')
print('|Tiros consecutivos| = 4/5 de dano')
print('|Tiro certeiro     | = 7/8 de dano')
print('|Tiro magico       | = 10 de dano')
print('+/- Usa mana')
time.sleep(1)
print('')
print('')
print('Mago      [3]')
print('|Em chamas!    | = 5/7 de dano')
print('|Absorva       | = 8/10 de dano')
print('|Pacto de sague| = 10/15 de dano')
print('*   Consome mana')
time.sleep(2)
print('\n')

while True:
    escolha = str(input('Escolha umas das classes pra ser a principal: '))
    if escolha in '123':
        break
    print('')
    print('\033[31mERRO: Digite umas das opções\033[m')
    time.sleep(0.5)
    print('')
    print('')

if escolha == '1':
    jogador = []
    jogador.append('Guerreiro')

elif escolha == '2':
    jogador = []
    jogador.append('Arqueiro')

elif escolha == '3':
    jogador = []
    jogador.append('Mago')

else:
    escolhe = random.choice(classe)
    jogador = []
    jogador.append(escolhe)


time.sleep(1)
print('\n')

print('━━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━━')
print(F'|Nome:     \033[31m{nome}\033[m       ')
print(f'|Classe:   \033[35m{jogador[0]}\033[m ')
print(f'|Dori:     \033[33m{Dori}\033[m       ')
print(f'|Mana:     \033[34m{mana}\033[m       ')
print(f'|HP:       \033[32m{HP}\033[m         ')
print('━━━━━─━━━━━━──━━━━━━⊱❉-⊰━━━━━━─━━━━━━─━━─━━━')

time.sleep(2)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')

cut = 0

XPB = 0
while True:
    if Vivo == 'Sim ele está':
        if HP > 0:
            Vivo = ''
            break

    elif Morte > 0:
        XP = 0
        HP = 30
        Nivel = 0
        mana = 50
        Dori = 0
        Morte = 0
        Mortes += 1


        intens.clear()
        intens.append('Poção pequena')
        print('Então o heroi morreu...')
        time.sleep(1)
        print(f'Contagem de mortes = {Mortes}')
        time.sleep(2)
        print(f'Agora eu pergunto {nome} você que continuar? É uma pergunta de S ou N')
        time.sleep(1)

        while True:
            contiar = str(input('Resposta: ')).upper()
            if contiar in 'SsNn':
                break
            print('')
            print('Parece que você errou ou não entendeu a pergunta oque eu pedi')
            time.sleep(3)
            print('Digite de S ou N')
            time.sleep(1)
            print('')
            print('')


        if contiar == 'N':
            print('A que triste gostaria de continuar vendo essa historia')
            time.sleep(3)
            print(f'Então tchau {nome}')
            ACABAR += 1
            time.sleep(2)
            break


        elif contiar == 'S':
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('\n')
            print('\n')
            time.sleep(1)


    while True:
        print('O heroi chegou na montanha')
        time.sleep(2)
        print('Subiu as escada e achou um goblin')
        time.sleep(2)
        print('Ele está protegendo a porta')
        time.sleep(2)
        print('\n')

        print('Oque vai fazer? ')
        print('|Atacar  | Atacar o goblin  [1]')
        print('|Esconder| Ir escondido     [2]')
        time.sleep(1)
        print('\n')

        while True:
            escolhe = str(input('Quais das opções você escolhe? '))
            if escolhe in '12':
                break
            print('')
            print('\033[31mERRO: Digite algumas das opções\033[m')
            time.sleep(0.5)
            print('')
            print('')

        if escolhe == '1':
            time.sleep(2)
            print('\n')
            hub(0)

            if HP <= 0:
                Morte += 1
                break

            if Fugir == True:
                print('O heroi da seu ultimo ataque acabando a luta')
                time.sleep(2)
                xp = random.randint(140, 145)
                XP += xp
                print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
                print('')
                time.sleep(3)
                print('Com o Goblin morto o heroi vasculhou o corpo do Goblin')
                time.sleep(2)
                dori = random.randint(25, 30)
                Dori += dori
                print(f'\033[33mE encontra {dori} de dori! O dori está DR:{Dori}\033[m')
                time.sleep(3)
                Fugir = False
                print('')
                print('Depois da luta o heroi segue sua viagem')
                time.sleep(2)

            elif Fugir == 'A':
                print('Como o heroi fugiu ele não ganhou nada...')
                time.sleep(2)
                Fugir = False
                print('Depois do heroi fugir da batalha ele continua a caminhar')
                time.sleep(3)

        elif escolhe == '2':
            print('')
            time.sleep(2)
            print('O heroi foi escondido')
            time.sleep(2)
            print('O goblin não percebeu sua presença')
            time.sleep(2)










        print('\n')
        print('\n')
        print('\n')
        print('\n')
        if cut == 0:
            print('Vozes: Foi ai que tudo começou')
            time.sleep(2)
            print('Vozes: O heroi abriu a porta')
            time.sleep(2)
            print('Vozes: Começando tudo')
            time.sleep(2)
            cut += 1    
        print('\n')
        print('\n')
        print('\n')
        print('\n')

        print('Uma sala onde tem duas portas')
        time.sleep(2)
        print('Em uma das portas tem um simbolo de um baú')
        time.sleep(3)
        print('E a outra porta é grande e vermelha')
        time.sleep(2)
        print('')
        print('Qual das duas portas você escolhe?')
        print('|Simbolo de baú|  [1]')
        print('|Grande porta  |  [2]')
        time.sleep(2)
        print('\n')

        while True:
            escolha = str(input('Escolha umas das opções: '))
            if escolha in '12':
                break
            print('')
            print('\033[31mERRO: Digite algumas das opções\033[m')
            time.sleep(0.5)
            print('')
            print('')
        print('\n')
        time.sleep(1)

        if escolha == '1':
            print('O heroi chega na sala')
            time.sleep(2)
            print('E lá está somente um baú')
            time.sleep(2)
            print('Será uma amardilha? Um deposito?')
            time.sleep(2)
            print('Só sabera se olhar')
            time.sleep(2)
            print('')
            while True:
                escolha = str(input('Deseja abrir o baú? [S/N]: ')).upper()
                if escolha in 'SN':
                    break
                print('')
                print('\033[31mERRO: Digite algumas das opções\033[m')
                time.sleep(0.5)
                print('')
                print('')

            time.sleep(1)
            print('')
            print('')
            
            if escolha == 'S':
                print('O heroi chega perto do baú')
                time.sleep(2)
                print('Abre ele e...')
                time.sleep(2)
                print('')
                randum = random.choice(bau)
                if randum == 'cobra':
                    print('Tem uma COBRA NO BAÚ!!!')
                    time.sleep(2)
                    print('Ela da um pulo do baú dando uma mordida no heroi')
                    time.sleep(2)
                    dano = random.randint(1, 4)
                    HP -= dano
                    time.sleep(2)
                    print('')
                    print('A cobra lhe deu dano')
                    time.sleep(2)
                    print(f'\033[31mMenos -{dano} de dano, seu HP está {HP}\033[m')
                    time.sleep(2)
                    print('\n')

                elif randum == 'dori':
                    dori = random.randint(10, 20)
                    time.sleep(1)
                    print(f'\033[33mO heroi encontra {dori} Dori!')
                    time.sleep(2)
                    print('')
                    Dori += dori
                    print(f'Seu dori está {Dori}\033[m')
                    time.sleep(2)
                    print('\n')
                
                elif randum == 'nada':
                    print('Não tinha simplismente nada de bom no baú')
                    time.sleep(2)
                    print('')
                    print('Só sujeira')
                    time.sleep(2)
                    print('\n')
                
                elif randum == 'Poção pequena':
                    print('O heroi encontra uma poção pequena de cura!')
                    time.sleep(2)
                    print('')
                    print('Quarda ou tomar a poção?')
                    print('|Quarda|  [1]')
                    print('|Tomar |  [2]')
                    time.sleep(3)
                    print('')
                    while True:
                        escolha = str(input('Oque você ira fazer? '))
                        if escolha in '12':
                            break
                        print('')
                        print('\033[31mERRO: Digite algumas das opções\033[m')
                        time.sleep(1)
                        print('')
                        print('')
                    
                    if escolha == '1':
                        intens.append('Poção pequena')
                        print('Poção pequena adicionada com sucesso!')
                        time.sleep(2)
                        print('\n')
                    
                    elif escolha == '2':
                        HP += 6
                        print('O heroi toma a poção pequena')
                        time.sleep(2)
                        print(f'\033[32mSeu HP está {HP}\033[m')
                        time.sleep(2)
                        print('\n')
                
                print('\n')
                time.sleep(2)
                print('O heroi volta da sala do baú e vai até a Grande porta')
                time.sleep(2)
                print('\n')
                print('\n')

                while True:
                    abrir = str(input('Aperte Enter/Enviar pra abrir a porta: '))
                    if abrir == '':
                        break
                    print('')
                    print(f'\033[31mERRO: Aperte Enter/Enviar\033[m')
                    time.sleep(1)
                    print('')
                    print('')

                if cutcine == 0:
                    time.sleep(3)
                    print('\n')
                    print('Está tudo escuro')
                    time.sleep(1)
                    print('Não da pra s-')
                    time.sleep(2)
                    print('')
                    print('\033[31m*BATIDA*\033[m')
                    print('')
                    time.sleep(2)
                    print('<Desconhecido>: Então mais um humano chegou até aqui')
                    time.sleep(2)
                    print('<Desconhecido>: Que azar o seu em?')
                    time.sleep(2)
                    print('')
                    print('*\033[33mTudo fica iluminado*\033[m')
                    print('')
                    time.sleep(2)
                    print('<Desconhecido>: ENCONTRA ', end='', flush=True)
                    time.sleep(1)
                    print('ALGUEM ', end='', flush=True)
                    time.sleep(1)
                    print('COMO ', end='', flush=True)
                    time.sleep(1)
                    print('\033[31mEU\033[m', end='', flush=True)
                    time.sleep(2)
                    print('')
                    print('')
                    print('Ele tem uma armadura e uma grande espada')
                    time.sleep(2)
                    print('Parece ser um cavaleiro')
                    time.sleep(2)
                    print('\n')
                    print('Oque vai fazer?')
                    print('|Atacar|  [1]')
                    print('|Fugir |  [2]')
                    time.sleep(2)
                    print('')
                    print('')
                    while True:
                        escolha = str(input('Oque você ira fazer? '))
                        if escolha in '12':
                            break
                        print('')
                        print('\033[31mERRO: Digite algumas das opções\033[m')
                        time.sleep(1)
                        print('')
                        print('')
                    print('')
                    time.sleep(2)
                    print('"Cavaleiro": Quem disse que você tem escolha?')
                    time.sleep(2)
                    print('"Cavaleiro": \033[31mHAHAHAHAHAHAHAHAHAHA\033[m')
                    time.sleep(3)
                    cutcine += 1
                    print('\n')

                elif cutcine == 1:
                    print('\n')
                    print('"Cavaleiro": EM GUARDA')
                    time.sleep(2)
                    print('\n')

                hub(1)
                if HP <= 0:
                    Morte += 1
                    break          

            elif escolha == 'N':

                time.sleep(2)
                print('')
                print('O heroi volta da sala do baú e vai até a Grande porta')
                time.sleep(2)
                print('\n')

                while True:
                    abrir = str(input('Aperte Enter/Enviar pra abrir a porta: '))
                    if abrir == '':
                        break
                    print('')
                    print(f'\033[31mERRO: Aperte Enter/Enviar\033[m')
                    time.sleep(1)
                    print('')
                    print('')

                if cutcine == 0:   
                    time.sleep(2)
                    print('\n')
                    print('Está tudo escuro')
                    print('Não da pra s-')
                    time.sleep(2)
                    print('')
                    print('\033[31m*BATIDA*\033[m')
                    print('')
                    time.sleep(2)
                    print('<Desconhecido>: Então mais um humano chegou até aqui')
                    time.sleep(2)
                    print('<Desconhecido>: Que azar o seu em?')
                    time.sleep(2)
                    print('')
                    print('*\033[33mTudo fica iluminado*\033[m')
                    print('')
                    time.sleep(2)
                    print('<Desconhecido>: ENCONTRA ', end='', flush=True)
                    time.sleep(1)
                    print('ALGUEM ', end='', flush=True)
                    time.sleep(1)
                    print('COMO ', end='', flush=True)
                    time.sleep(1)
                    print('\033[31mEU\033[m', end='', flush=True)
                    time.sleep(2)
                    print('')
                    print('')
                    print('Ele tem uma armadura e uma grande espada')
                    time.sleep(2)
                    print('Parece ser um cavaleiro')
                    time.sleep(2)
                    print('\n')
                    print('Oque vai fazer?')
                    print('|Atacar|  [1]')
                    print('|Fugir |  [2]')
                    time.sleep(2)
                    print('')
                    print('')

                    while True:
                        escolha = str(input('Oque você ira fazer? '))
                        if escolha in '12':
                            break
                        print('')
                        print('\033[31mERRO: Digite algumas das opções\033[m')
                        time.sleep(1)
                        print('')
                        print('')

                    time.sleep(2)
                    print('')
                    print('"Cavaleiro": Quem disse que você tem escolha?')
                    time.sleep(2)
                    print('"Cavaleiro": \033[31mHAHAHAHAHAHAHAHAHAHA\033[m')
                    time.sleep(3)
                    cutcine += 1
                    print('\n')

                elif cutcine == 1:
                    print('\n')
                    print('"Cavaleiro": EM GUARDA')
                    time.sleep(2)
                    print('\n')

                hub(1)
                if HP <= 0:
                    Morte += 1
                    break


        elif escolha == '2':
            while True:
                abrir = str(input('Aperte Enter/Enviar pra abrir a porta: '))
                if abrir == '':
                    break
                print('')
                print(f'\033[31mERRO: Aperte Enter/Enviar\033[m')
                time.sleep(1)
                print('')
                print('')

            if cutcine == 0:
                print('')
                print('O heroi vai até a porta e abre ela')
                time.sleep(3)
                print('\n')
                print('Está tudo escuro')
                print('Não da pra s-')
                time.sleep(2)
                print('')
                print('\033[31m*BATIDA*\033[m')
                print('')
                time.sleep(2)
                print('<Desconhecido>: Então mais um humano chegou até aqui')
                time.sleep(2)
                print('<Desconhecido>: Que azar o seu em?')
                time.sleep(2)
                print('')
                print('*\033[33mTudo fica iluminado*\033[m')
                print('')
                time.sleep(2)
                print('<Desconhecido>: ENCONTRA ', end='', flush=True)
                time.sleep(1)
                print('ALGUEM ', end='', flush=True)
                time.sleep(1)
                print('COMO ', end='', flush=True)
                time.sleep(1)
                print('\033[31mEU\033[m', end='', flush=True)
                time.sleep(2)
                print('')
                print('')
                print('Ele tem uma armadura e uma grande espada')
                time.sleep(2)
                print('Parece ser um cavaleiro')
                time.sleep(2)
                print('\n')
                print('Oque vai fazer?')
                print('|Atacar|  [1]')
                print('|Fugir |  [2]')
                time.sleep(2)
                print('')
                print('')
                while True:
                    escolha = str(input('Oque você ira fazer? '))
                    if escolha in '12':
                        break
                    print('')
                    print('\033[31mERRO: Digite algumas das opções\033[m')
                    time.sleep(1)
                    print('')
                    print('')
                print('')
                time.sleep(2)
                print('"Cavaleiro": Quem disse que você tem escolha?')
                time.sleep(2)
                print('"Cavaleiro": \033[31mHAHAHAHAHAHAHAHAHAHA\033[m')
                time.sleep(3)
                cutcine += 1
                print('\n')
            
            elif cutcine == 1:
                print('"Cavaleiro": EM GUARDA')
                time.sleep(2)
                print('\n')

            hub(1)
            if HP <= 0:
                Morte += 1
                break
            
        print('\n')
        time.sleep(1)
        print('"Cavaleiro": N-não NÃO co-como')
        time.sleep(2)
        print('"Cavaleiro": UM HUMANO GANHOU DE MIM')
        time.sleep(2)
        print('"Cavaleiro": EU SOU MAIS FORTE, E-ELE FALOU PRA MIM')
        time.sleep(2)
        print('*Ele está muito fraco*')
        time.sleep(2)
        print('"Cavaleiro": Insolente você verá, eu não vou morrer, NÃO ASSIM')
        time.sleep(3)
        print('*O cavaleiro que era tão confiante, corre saindo da sala*')
        time.sleep(3)
        print('\n')

        xp = random.randint(210, 215)
        XP += xp

        print('\n')
        nivel()
        print('\n')

        print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
        print('')
        time.sleep(3)
        print('O cavaleiro deixou cair alguns doris o heroi pega')
        dori = random.randint(35, 40)
        Dori += dori
        print(f'\033[33m{dori} A mais de dori o dori está DR:{Dori}\033[m')
        time.sleep(3)   











        print('\n')
        print('Depois dessa grande luta')
        time.sleep(2)
        print('O heroi continua a caminhar')
        time.sleep(2)
        print('A visão do heroi está')
        time.sleep(2)
        print('Escurecendo...')
        time.sleep(2)
        print('Mais e mais...')
        print('')
        time.sleep(2)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', flush=True)
        time.sleep(2)
        print('*O heroi desacordou*')
        time.sleep(2)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('Vozes: Imagina um heroi onde')
        time.sleep(2)
        print('Vozes: Mata todos os inimigos?')
        time.sleep(2)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print('*O heroi acordou*')
        print('')
        print('<Desconhecido>: A finalmente acordou')
        time.sleep(2)
        print('<Desconhecido>: Odeio aquele cara')
        time.sleep(3)
        print('<Desconhecido>: Foi ele que te evenenou')
        time.sleep(2)
        print('<Desconhecido>: A me desculpa nem me apresentei')
        time.sleep(3)
        print('<Desconhecido>: Meu nome é Charlie, Charlie o vendedor')
        time.sleep(3)
        print('\n')
        print('Charlie: Estou aqui pra ajudar pessoas como você')
        time.sleep(3)
        print('Charlie: Que veio até aqui pra ganhar o Mago ', end='', flush=True)
        time.sleep(3)
        print('(Apesar que nunca consequem...)')
        time.sleep(2)
        print('Charlie: Eu tenho boas coisas pra você venha ver')
        time.sleep(4)
        print('\n')
        print('\n')
        print('\n')


        while True:
            print('==================') 
            print('Loja do Charlie: ')
            print('==================')
            print('|Intens  | = [1]')
            print('|Armas   | = |2|')  
            print('|Conversa| = [3]')
            print('|Sair    | = [4]')
            print('==================')
            time.sleep(3)
            print('\n')


            while True:
                escolha = str(input('Oque você vai fazer? '))
                if escolha in '1234':
                    break
                print('')
                print('\033[31mERRO: Escolha uma das opções\033[m')
                time.sleep(1)
                print('')
                print('')
            print('\n')
            

            if escolha == '1':
                while True:
                    print('=================================')
                    print('Comprar intens: ')
                    print('=================================')
                    print('|Poção de cura P| >DR:13< = [1]')
                    print('|Poção de mana P| >DR:15< = [2]')
                    print('|Sair           |         = [3]')
                    print('=================================')
                    time.sleep(3)
                    print('\n')

                    while True:
                        escolha = str(input('Oque você vai fazer? '))
                        if escolha in '123':
                            break
                        print('')
                        print('\033[31mERRO: Escolha uma das opções\033[m')
                        time.sleep(1)
                        print('')
                        print('')
                    print('\n')
                    


                    if escolha == '1':
                        if Dori >= 13:
                            print('O heroi quardou a poção em sua bolsa')
                            intens.append('Poção pequena')
                            time.sleep(2)
                            Dori -= 13
                            print(f'\033[33mSeu dori está DR:{Dori}\033[m')
                            time.sleep(2)
                            print('Charlie: Obigado pelo dinheiro amigo')
                            time.sleep(2)
                            print('\n')

                        elif Dori < 13:
                            print('Charlie: Pelo que parece você não tem dori o bastante')
                            time.sleep(3)
                            diminição = Dori - 13
                            print(f'Pra o valor da poção pequena você precisa de DR:{diminição}')
                            time.sleep(3)
                            print('\n')
                    


                    elif escolha == '2':
                        if Dori >= 15:
                            print('O heroi quardou a poção em sua bolsa')
                            intens.append('Poção de mana')
                            time.sleep(2)
                            Dori -= 15
                            print(f'\033[33mSeu dori está DR:{Dori}\033[m')
                            time.sleep(2)
                            print('Charlie: Obigado pelo dinheiro amigo')
                            time.sleep(2)
                            print('\n')

                        elif Dori < 15:
                            print('Charlie: Pelo que parece você não tem dori o bastante')
                            time.sleep(3)
                            diminição = Dori - 15
                            print(f'Pra o valor da poção pequena você precisa de DR:{diminição}')
                            time.sleep(3)
                            print('\n') 


                    elif escolha == '3':
                        break             

            
            elif escolha == '2':
                print('Ainda não estou vendendo armas')
                time.sleep(2)
                print('Mais logo logo eu vou!')
                time.sleep(2)
                print('\n')

            elif escolha == '3':
                print('============================================')
                print('Convesar: ')
                print('============================================')
                print('"Qual o nome do cavaleiro?         "  = [1]')
                print('"Que tipo de veneno que ele me deu?"  = [2]')
                print('"Por que bota preço nas vendas?    "  = [3]')
                print('============================================')
                time.sleep(3)
                print('\n')

                while True:
                    escolha = str(input('Oque quer perguntar? '))
                    if escolha in '123':
                        break
                    print('')
                    print('\033[31mERRO: Escolha uma das opções\033[m')
                    time.sleep(1)
                    print('')
                    print('')
                
                if escolha == '1':
                    print('Charlie: Cavaleiro? Assim você fala dele')
                    time.sleep(2)
                    print('Charlie: Meio que não sei o nome dele haha')
                    time.sleep(2)
                    print('Charlie: Eu ja me debati com ele')
                    time.sleep(2)
                    print('Charlie: Tentou me matar por isso nem da pra saber o nome dele')
                    time.sleep(3)
                    print('\n')
                
                elif escolha == '2':
                    print('Charlie: O veneno que ele lhe deu foi naverdade uma magia de veneno')
                    time.sleep(2)
                    print('Charlie: Que é fabricada por uma aranha rainha')
                    print('Charlie: Nunca me meti lá')
                    time.sleep(3)
                    print('\n')
                
                elif escolha == '3':
                    print('Charlie: É serio? Ta realmente me fazendo essa pergunta')
                    time.sleep(2)
                    print('Charlie: Pra conseguir dori ue')
                    time.sleep(2)
                    print('Charlie: Eu de fez em quando vou pra minha vila e compro coisa lá')
                    time.sleep(2)
                    print('Charlie: Mais isso é assunto pra outro papo')
                    time.sleep(2)
                    print('\n')
            

            elif escolha == '4':
                print('Charlie: Então ta certo amigo')
                time.sleep(2)
                print('Charlie: Espero que eu te encontre mais vezes')
                time.sleep(2)
                print('Charlie: Não morra até lá hahahaha ')
                time.sleep(2)
                break
        
        print('\n')
        print('Parte 1 acabada')
        print('\n')
        print('\n')
        print('\n')
        print('\n')

        Vivo = 'Sim ele está'

        NivelB = Nivel
        XPB = XP

        del intensB
        intensB = intens[:]

        break











print('\n')
print('\n')
print('\n')
print('O heroi encontrou um poço dos sonhos')
time.sleep(2)
print('Tem uma placa dizendo "Descanse nimguem podera te atrapalhar"')
time.sleep(2)
print('O heroi ainda cansado descansa lá mesmo')
time.sleep(2)

if Nivel == 1:
    HP = 32
    mana = 60

elif Nivel == 2: 
    HP = 33
    mana = 70

print('\033[32mHP MAX\033[m, \033[34mMANA MAX\033[m')
time.sleep(3)
print('\n')


print('\n')
print('\n')
print('\n')

print('Quando acorda')
time.sleep(2)
print('O HEROI ESTÁ PRESO?')
time.sleep(2)
print('Numa teia de aranha!')
time.sleep(2)
print('Tem uma aranha chegando')
time.sleep(2)
print('Ela está chegando mais e mais perto')
time.sleep(3)
print('Uma flecha acerta a aranha')
time.sleep(2)
print('E as teias que prediam o heroi foi cortada')
time.sleep(3)
print('Apesar de não saber oque aconteceu')
time.sleep(2)
print('O heroi continua a caminhar')
time.sleep(2)
print('\n')


matando = 0
cutcine = 0
while True:
    Dori2 = Dori
    Nivel2 = Nivel

    if Vivo == 'Sim ele está':
        if HP > 0:
            Vivo = ''
            break

    elif Morte > 0:
        matando = 0
        HP = 30
        Nivel = NivelB
        XP = XPB
        if Nivel == 1:
            HP = 32
            mana = 60
            Nivel = 1
        elif Nivel == 2:
            HP = 33
            mana = 70
            Nivel = 2

        del intens
        intens = intensB[:]


        Dori2 = Dori
        Morte = 0
        Mortes += 1



        print('Então o heroi morreu...')
        time.sleep(1)
        print(f'contagem de mortes = {Mortes}')
        time.sleep(2)
        print(f'Agora eu pergunto {nome} você que continuar? É uma pergunta de S ou N')
        time.sleep(1)

        while True:
            contiar = str(input('Resposta: ')).upper()
            if contiar in 'SsNn':
                break
            print('')
            print('Parece que você errou ou não a pergunta entendeu oque eu pedi')
            time.sleep(3)
            print('Digite de S ou N')
            time.sleep(1)
            print('')
            print('')


        if contiar == 'N':
            print('A que triste gostaria de continuar vendo essa historia')
            time.sleep(1)
            print(f'Então tchau {nome}')
            ACABAR += 1
            time.sleep(1)
            break


        elif contiar == 'S':
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('\n')
            print('\n')
            time.sleep(1)

    while True:
        pagou = ''
        print('E ele se depara com uma estatua de uma aranha')
        time.sleep(3)
        print('Com uma placa dizendo:')
        time.sleep(3)
        print('Pague 50 dori e tenha minha gratidão')
        time.sleep(3)
        print('')
        print('')

        while True:
            escolha = str(input('Que paga os 50 de dori? [S/N]: '))
            if escolha in 'SsNn':
                break
            print('')
            print('\033[31mERRO: Digite entre S ou N\033[m')
            time.sleep(2)
            print('')
            print('')
        
        print('')
        print('')
        if escolha in 'Ss':

            if Dori2 >= 50:
                print('O heroi deixa o dinheiro e se ajuelha')
                time.sleep(3)
                print('(nada aconteceu?)')
                time.sleep(2)
                print('O heroi se levanta e continua caminhando')
                time.sleep(3)
                Dori2 -= 50
                print(f'\033[33mDR:{Dori2}\033[m')
                time.sleep(2)
                pagou = ''
                pagou = 'sim'
                print('\n')
                

            elif Dori2 < 50:
                while True:
                    print('O heroi não tem dinheiro suficiente')
                    time.sleep(2)
                    escolha = str(input('Ainda assim quer pagar? [S/N]: '))
                    time.sleep(2)

                    if escolha in 'SsNn':
                        break
                    print('')
                    print('\033[31mERRO: Digite entre S ou N\033[m')
                    time.sleep(2)
                    print('')
                    print('')
                
                if escolha in 'Ss':
                    print('O heroi deixa todo o seu dinheiro lá')
                    time.sleep(3)
                    print('(Nada aconteceu)')
                    time.sleep(2)
                    print('E continua a caminhar')
                    time.sleep(3)
                    Dori2 -= Dori2
                    print(f'\033[33mDR:{Dori2}\033[m')
                    time.sleep(2)
                    print('\n')
                    pagou = 'N'
                
                elif escolha in 'Nn':
                    print('O heroi passa reto e continua o caminho')
                    time.sleep(2)
                    print('\n')
        
        elif escolha in 'Nn':
            print('O heroi passa reto e continua o caminho')
            time.sleep(2)
            print('\n')
        
        print('\n')
        print('\n')
        print('\n')
        time.sleep(1)
        print('No caminho o heroi encontra')
        time.sleep(2)
        print('3 Pequenas aranhas')
        time.sleep(2)
        print('(Parecem não querer lutar)')
        time.sleep(2)

        while True:
            escolha = str(input('Ainda assim quer atacar elas? [S/N]: '))
            if escolha in 'SsNn':
                break
            print('')
            print('\033[31mERRO: Digite entre S ou N\033[m')
            time.sleep(2)
            print('')
            print('')
        
        aranhas = 3
        if escolha in 'Ss':
            aranhas = 3
            while True:
                print('\n')
                print('='*40)
                print('HUB de opções:')
                print('='*40)
                print('|Matar | [1]')
                print('|Itens | [2]')
                print('|Defesa| [3]')
                print('|Poupar| [4]')
                print('='*40)
                time.sleep(2)
                print('\n')

                while True:
                    hub1 = str(input('Digite algumas das opções: '))
                    if hub1 in '1234':
                        break
                    print('')
                    print('\033[31mErro: Digite umas das opções\033[m')
                    time.sleep(0.5)
                    print('')
                    print('')
                time.sleep(2)
                print('\n')

                if hub1 == '1':
                    if aranhas == 3:
                        print('\033[31mO heroi matou a primeira aranha\033[m')
                        time.sleep(2)
                    elif aranhas == 2:
                        print('\033[31mO heroi matou a segunda aranha\033[m')
                        time.sleep(2)
                    elif aranhas == 1:
                        print('\033[31mO heroi matou a ultima aranha\033[m')
                    aranhas -= 1

                elif hub1 == '2':
                    print('O heroi não precisa de uma poção')
                    time.sleep(2)

                elif hub1 == '3':
                    print('Não é necessario defender aqui')
                    time.sleep(2)
                
                elif hub1 == '4':
                    print(f'O heroi popou as {aranhas} aranhas')
                    time.sleep(2)
                    break

                if aranhas == 0:
                    print('')
                    print('')
                    print('O heroi matou as 3 aranhas')
                    time.sleep(2)
                    print('Alias elas são \033[31mMONSTROS\033[m né?')
                    time.sleep(2)
                    break
                
                print('')
                print('')
                if aranhas == 3:
                    print('Elas são fracas')
                    time.sleep(2)
                    print('Não consegue atacar o heroi')
                    time.sleep(2)
                elif aranhas == 2:
                    print('As duas querem se junta pra atacar o heroi')
                    time.sleep(3)
                    print('Mais são fracas pra isso')
                    time.sleep(2)
                elif aranhas == 1:
                    print('A ultima olha o heroi com uma cara triste')
                    time.sleep(3)

            
            if aranhas == 0:
                print('\n')
                print('Com as 3 aranhas mortas')
                time.sleep(2)
                print('O heroi continu-')
                time.sleep(2)
                print('')
                print('*A mãe das 3 aranhas apareceu*')
                print('')
                time.sleep(2)
                print('Ela não fala nada, pós monstros fracos não falam')
                time.sleep(3)
                print('O heroi não tem escolha')
                time.sleep(2)
                print('A não ser lutar')
                time.sleep(2)


                print('\n')
                hub(2)
                if HP <= 0:
                    Morte += 1
                    break
                
                matando += 4
                print('\n')
                print('A aranha mãe, morreu')
                time.sleep(2)
                print('O heroi não ganhou nada')
                time.sleep(2)
                print('Mata todas aqueles monstros realmente valeu a pena?')
                time.sleep(3)
                print('Ou so foi uma perda de tempo?')
                time.sleep(2)

                print('\n')

                print('O heroi continua a caminhar')
            
            else:
                print('O heroi passa reto por elas')
                time.sleep(2)
                print('Elas se escondem do heroi')
                time.sleep(2)
            

        elif escolha in 'Nn':
            print('O heroi passa por elas')
            time.sleep(2)
            print('E elas não fizeram nada')
            time.sleep(2)
            print('\n')

        time.sleep(2)
        print('\n')
        print('O heroi continua a caminhar mais e mais')
        time.sleep(3)
        print('Sem encontra nada')
        time.sleep(2)
        print('Só mais e mais telhas de aranhas')
        time.sleep(2)
        print('Esse caminho é gigantesco')
        time.sleep(2)
        print('')
        print('')

        print('E quando menos espera uma aranha aparece')
        time.sleep(3)
        print('Ela corre atrás do heroi')
        time.sleep(2)
        print('O heroi não tem opção a não ser lutar')
        time.sleep(3)


        print('\n')
        hub(3)
        if HP <= 0:
            Morte += 1
            break
        print('\n')
        time.sleep(2)

        if Fugir == 'A':
            print('O heroi fugiu da batalha...')
            time.sleep(2)
            Fugir = False
            print('Com isso não ganhou nada')
            time.sleep(2)
        
        else:
            print('O heroi termina com seu ultimo ataque')
            time.sleep(3)
            xp = random.randint(140, 160)
            XP += xp

            print('\n')
            nivel()
            print('\n')

            print('')
            matando += 1
            print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
            print('')
            time.sleep(3)
            print('Com a aranha morta o heroi vasculhou o corpo dela')
            dori = random.randint(20, 25)
            Dori2 += dori
            print(f'\033[33mE encontra {dori} de dori! O dori está DR:{Dori2}\033[m')
            time.sleep(3)
            Fugir = False
            print('')
            print('Depois da luta o heroi segue sua viagem')
            time.sleep(1)
        
        print('\n')
        print('\n')
        print('\n')
        print('O heroi encontrou uma grande porta')
        time.sleep(2)
        print('Só um corredor uma porta e nada mais')
        time.sleep(3)
        print('Por algum motivo o heroi se sente')
        time.sleep(2)
        print('Com medo, de algo')
        time.sleep(2)
        print('Quanto mais chega perto da porta')
        time.sleep(3)
        print('Mais desse sentimento aparece...')
        time.sleep(3)
        print('\n')
        
        print('Não tem mais nada pra fazer a não ser')
        time.sleep(3)
        print('Abrir a porta')
        time.sleep(2)

        while True:
            porta = str(input('Aperte Enter/Enviar para abrir a porta: '))
            if porta == '':
                break
            print('')
            print(f'\033[31mERRO: Aperte Enter/Enviar\033[m')
            time.sleep(1)
            print('')
            print('')
        
        if cutcine == 0:
            time.sleep(3)
            print('\n')
            print('Quando abre a porta')
            time.sleep(2)
            print('É uma grande sala')
            time.sleep(2)
            print('Com muita teia de aranha')
            time.sleep(2)
            print('Está tudo escuro')
            time.sleep(2)
            print('')
            print('*Olhos vermelhos aparece na escuridão*')
            print('')
            time.sleep(2)
            print('O heroi ainda não consegue reconhecer oque é')
            time.sleep(4)
            print('\n')
            cutcine += 1
        elif cutcine == 1:
            print('Olhos aparece na escuridão')
            time.sleep(2)
            print('\n')

        if pagou == 'sim':
            if matando < 5:
                print('<Desconhecida>: Obrigada')
                time.sleep(2)
                print('<Desconhecida>: Por ter pagado o dinheiro')
                time.sleep(2)
                print('<Desconhecida>: Você é uma boa pessoa')
                time.sleep(2)
                
                print('')
                print('')
                print('<Desconhecida>: Eu tenho um presente pra você viajante')
                time.sleep(3)
                print('*Uma adaga*')
                time.sleep(2)
                print('<Desconhecida>: Isso é uma adaga que envenena')
                time.sleep(2)
                print('Com ataques furtivos')
                time.sleep(2)
                print('<Desconhecida>: Você pode trocar ela por sua arma que você está')
                time.sleep(3)

                print('\n')

                while True:
                    escolha = str(input('Quer troca sua arma por essa? [S/N]'))
                    if escolha in 'SsNn':
                        break
                    print('')
                    print('\033[31mERRO: Digite entre S ou N\033[m')
                    time.sleep(2)
                    print('')
                    print('')
                
                if escolha in 'Ss':
                    print('O heroi pega a adaga')
                    time.sleep(2)
                    print('Joga a arma que estava e guarda a adaga')
                    time.sleep(2)
                    print('Ele se sente como ja tivesse usado ela muitas vezes...')
                    time.sleep(3)
                    jogador.clear()
                    jogador.append('Assasino')
                
                elif escolha in 'Nn':
                    print('O heroi recursa a oferta')
                    time.sleep(2)
                    print('Rainha: A entendo não vou te culpar')
                    time.sleep(2)
                    print('Rainha: Pode seguir o seu caminho')
                    time.sleep(2)

            
            elif matando == 5:
                print('<Desconhecido>: Você pode até te pagado')
                time.sleep(2)
                print('*Ela sabe oque você fez*')
                time.sleep(2)
                print('<Desconhecido>: MAIS EU NÃO TE PERDOAR')
                time.sleep(2)
                print('<Desconhecido>: POR QUE')
                time.sleep(2)
                print('<Desconhecido>: VOCÊ MATOU ELAS')
                time.sleep(2)
                print('<Desconhecido>: \033[31mMORRA\033[m')
                time.sleep(2)
                print('\n')

                hub(5)
                if HP <= 0:
                    Morte += 1
                    break
                
                print('\n')
                print('O <Desconhecido> Morreu')
                time.sleep(2)
                print('Umas das aranhas: M-Minha rainha')
                time.sleep(2)
                print('*Ela olha pra você*')
                time.sleep(2)
                print('Umas das aranhas: Por que você fez isso')
                time.sleep(2)
                print('Umas das aranhas: VOCÊ NOS CHAMA DE MONSTRO')
                time.sleep(3)
                print('Umas das aranhas: MAIS O VERDADEIRO MONSTRO AQUI É VOCÊ')
                time.sleep(3)
                print('Umas das aranhas: OLHA O TANTO DE NOIS QUE VOCÊ MATOU')
                time.sleep(3)
                print('\n')

                print('Umas das aranhas: EI PARA DE VIM PRA CÁ')
                time.sleep(2)
                print('Umas das aranhas: OQUE VOCÊ VA-')
                time.sleep(2)
                print('\033[31m-14 de dano\033[m')
                time.sleep(4)
                print('\n')


                print('Seu poder está maior')
                time.sleep(2)
                print('\033[35mSeu nivel está 5\033[m')
                time.sleep(2)
                print('\033[33mDR:112\033[m')
                time.sleep(2)
                Dori2 = 112
                Dori = 112
                Nivel = 5
                XP = 620

                print('\n')
                time.sleep(2)
                print('Você não pode mais mudar de caminho')
                time.sleep(2)
                print('Mate, Mate todos')
                time.sleep(2)
                print('Vozes: Seja forte')
                time.sleep(2)







        elif matando == 5:
            print('<Desconhecido>: MONSTRO')
            time.sleep(2)
            print('*Ela sabe oque você fez*')
            time.sleep(2)
            print('<Desconhecido>: VOCÊ MATOU ELAS')
            time.sleep(2)
            print('<Desconhecido>: POR QUE')
            time.sleep(2)
            print('<Desconhecido>: ESSE É SEU FIM')
            time.sleep(2)
            print('<Desconhecido>: \033[31mMORRA\033[m')
            time.sleep(2)
            print('\n')

            hub(5)
            if HP <= 0:
                Morte += 1
                break
            
            print('\n')
            print('O <Desconhecido> Morreu')
            time.sleep(2)
            print('Umas das aranhas: M-Minha rainha')
            time.sleep(2)
            print('*Ela olha pra você*')
            time.sleep(2)
            print('Umas das aranhas: Por que você fez isso')
            time.sleep(2)
            print('Umas das aranhas: VOCÊ NOS CHAMA DE MONSTRO')
            time.sleep(3)
            print('Umas das aranhas: MAIS O VERDADEIRO MONSTRO AQUI É VOCÊ')
            time.sleep(3)
            print('Umas das aranhas: OLHA O TANTO DE NOIS QUE VOCÊ MATOU')
            time.sleep(3)
            print('\n')

            print('Umas das aranhas: EI PARA DE VIM PRA CÁ')
            time.sleep(2)
            print('Umas das aranhas: OQUE VOCÊ VA-')
            time.sleep(2)
            print('\033[31m-14 de dano\033[m')
            time.sleep(4)
            print('\n')


            print('Seu poder está maior')
            time.sleep(2)
            print('\033[35mSeu nivel está 5\033[m')
            time.sleep(2)
            print('\033[33mDR:112\033[m')
            time.sleep(2)
            Dori2 = 112
            Dori = 112
            Nivel = 5
            XP = 620

            print('\n')
            time.sleep(2)
            print('Você não pode mais mudar de caminho')
            time.sleep(2)
            print('Mate, Mate todos')
            time.sleep(2)
            print('Vozes: Seja forte')
            time.sleep(2)






        else:
            print('<Desconhecido>: Pelo visto você não pagou')
            time.sleep(2)
            print('<Desconhecido>: Então não tera minha gratidão')
            time.sleep(2)
            print('<Desconhecido>: MORRA')
            time.sleep(2)
            print('\n')

            hub(4)
            if HP <= 0:
                Morte += 1
                break

            print('<Desconhecido>: Haha isso foi uma boa luta')
            time.sleep(2)
            print('<Desconhecido>: Faz tempo que não tenho uma dessas')
            time.sleep(3)
            print('<Desconhecido>: Eu sou a rainha desse lugar')
            time.sleep(2)
            print('Rainha: Pode me chamar de rainha')
            time.sleep(2)
            print('Rainha: Como recompensa por te lutado com migo')
            time.sleep(3)
            print('Rainha: Tenho um presente')
            time.sleep(2)
            print('')
            print('*Uma adaga*')
            print('')
            time.sleep(2)
            print('Rainha: Isso é uma adaga que envenena')
            time.sleep(2)
            print('Com ataques furtivos')

            print('')

            while True:
                escolha = str(input('Quer troca sua arma por essa? [S/N]'))
                if escolha in 'SsNn':
                    break
                print('')
                print('\033[31mERRO: Digite entre S ou N\033[m')
                time.sleep(2)
                print('')
                print('')
            
            if escolha in 'Ss':
                print('O heroi pega a adaga')
                time.sleep(2)
                print('Joga a arma que estava e guarda a adaga')
                time.sleep(2)
                print('Ele se sente como ja tivesse usado ela muitas vezes...')
                time.sleep(3)
                jogador.clear()
                jogador.append('Assasino')
            
            elif escolha in 'Nn':
                print('O heroi recursa a oferta')
                time.sleep(2)
                print('Rainha: A entendo não vou te culpar')
                time.sleep(2)
                print('Rainha: Pode seguir o caminho')
                time.sleep(2)


            time.sleep(2)
            print('\n')
            xp = random.randint(200, 225)
            XP += xp
            print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')

            print('\n')
            nivel()
            print('\n')

            time.sleep(3)
            Fugir = False



        print('\n')
        time.sleep(2)
        print('O heroi chega ao vim desse caminho')
        time.sleep(2)
        Vivo = 'Sim ele está'
        print('Parte 2 acabada')
        time.sleep(4)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        NivelB = Nivel
        XPB = XP

        break



print('\n')
Dori = Dori2

print('Charlie: UFA')
time.sleep(2)
print('Charlie: Hoje eu pensava que eu ia morre')
time.sleep(2)
print('Charlie: VIAJANTE!')
time.sleep(2)
print('Charlie: Eu tenho uma novidade')
time.sleep(2)
print('Charlie: De armas!!!')
time.sleep(2)
print('\n')


while True:
    print('===================') 
    print('Loja do Charlie: ')
    print('===================')
    print('|Intens  | = [1]')
    print('|Armas   | = |2|')  
    print('|Conversa| = [3]')
    print('|Sair    | = [4]')
    print('===================')
    time.sleep(3)
    print('\n')


    while True:
        escolha = str(input('Oque você vai fazer? '))
        if escolha in '1234':
            break
        print('')
        print('\033[31mERRO: Escolha uma das opções\033[m')
        time.sleep(1)
        print('')
        print('')
    print('\n')
            

    if escolha == '1':
        while True:
            print('=================================')
            print('Comprar intens: ')
            print('=================================')
            print('|Poção de cura P| >DR:13< = [1]')
            print('|Poção de cura M| >DR:17< = [2]')
            print('|Poção de mana P| >DR:15< = [3]')
            print('|Sair           |         = [4]')
            print('=================================')
            time.sleep(3)
            print('\n')

            while True:
                escolha = str(input('Oque você vai fazer? '))
                if escolha in '1234':
                    break
                print('')
                print('\033[31mERRO: Escolha uma das opções\033[m')
                time.sleep(1)
                print('')
                print('')
            print('\n')
                    


            if escolha == '1':
                if Dori >= 13:
                    print('O heroi quardou a poção em sua bolsa')
                    intens.append('Poção pequena')
                    time.sleep(2)
                    Dori -= 13
                    print(f'\033[33mSeu dori está DR:{Dori}\033[m')
                    time.sleep(2)
                    print('Charlie: Obigado pelo dinheiro amigo')
                    time.sleep(2)
                    print('\n')

                elif Dori < 13:
                    print('Charlie: Pelo que parece você não tem dori o bastante')
                    time.sleep(3)
                    diminição = Dori - 13
                    print(f'Pra o valor da poção pequena você precisa de DR:{diminição}')
                    time.sleep(3)
                    print('\n')
                    
            elif escolha == '3':
                if Dori >= 15:
                    print('O heroi quardou a poção em sua bolsa')
                    intens.append('Poção de mana')
                    time.sleep(2)
                    Dori -= 15
                    print(f'\033[33mSeu dori está DR:{Dori}\033[m')
                    time.sleep(2)
                    print('Charlie: Obigado pelo dinheiro amigo')
                    time.sleep(2)
                    print('\n')

                elif Dori < 15:
                    print('Charlie: Pelo que parece você não tem dori o bastante')
                    time.sleep(3)
                    diminição = Dori - 15
                    print(f'Pra o valor da poção pequena você precisa de DR:{diminição}')
                    time.sleep(3)
                    print('\n') 


            elif escolha == '2':
                if Dori >= 17:
                    print('O heroi quardou a poção em sua bolsa')
                    intens.append('Poção media  ')
                    time.sleep(2)
                    Dori -= 17
                    print(f'\033[33mSeu dori está DR:{Dori}\033[m')
                    time.sleep(2)
                    print('Charlie: Obigado pelo dinheiro amigo')
                    time.sleep(2)
                    print('\n')

                elif Dori < 17:
                    print('Charlie: Pelo que parece você não tem dori o bastante')
                    time.sleep(3)
                    diminição = Dori - 17
                    print(f'Pra o valor da poção media você precisa de DR:{diminição}')
                    time.sleep(3)
                    print('\n') 



            elif escolha == '4':
                break             

            
    elif escolha == '2':
            print('=================================')
            print('Comprar armas: ')
            print('=================================')
            print('|Espada e moeda| >DR:30< = [1]')
            print('|Machado       | >DR:25< = [2]')
            print('|Sair          |         = [3]')
            print('=================================')
            time.sleep(3)
            print('\n')


            while True:
                escolha = str(input('Oque você vai comprar? '))
                if escolha in '123':
                    break
                print('')
                print('\033[31mERRO: Escolha uma das opções\033[m')
                time.sleep(1)
                print('')
                print('')
            print('\n')

            if escolha == '1':
                if Dori >= 30:
                    Dori -= 30
                    print('Charlie: Essa arma é bem estranhas')
                    time.sleep(2)
                    print('Charlie: A moeda não é normal tem algo de diferente nela')
                    time.sleep(2)
                    print('Charlie: E essa espada nunca vi uma dessa')
                    time.sleep(2)
                    print('')

                    print('O heroi joga arma que está')
                    time.sleep(2)
                    print('E pega a espada com a moeda')
                    time.sleep(2)
                    print('Ele se sente como ja tivesse usado ele')
                    time.sleep(2)
                    jogador.clear()
                    jogador.append('Chance')
                    print('')
                    print(f'\033[33mSeu dori está {Dori}\033[m')
                
                elif Dori < 30:
                    print('Charlie: Pelo que parece você não tem dori o bastante')
                    time.sleep(3)
                    diminição = Dori - 30
                    print(f'Pra o valor da espada e moeda você precisa de DR:{diminição}')
                    time.sleep(3)
                    print('\n') 

                print('\n')


            
            elif escolha == '2':
                if Dori >= 25:
                    Dori -= 25
                    print('Charlie: Esse machado é bem pesado')
                    time.sleep(2)
                    print('Charlie: Com isso muito forte')
                    time.sleep(2)
                    print('')

                    print('O heroi joga arma que está')
                    time.sleep(2)
                    print('E pega o machado')
                    time.sleep(2)
                    print('Ele se sente como ja tivesse usado ele')
                    time.sleep(2)
                    jogador.clear()
                    jogador.append('Bárbaro')
                    print('')
                    print(f'\033[33mSeu dori está {Dori}\033[m')

                elif Dori < 30:
                    print('Charlie: Pelo que parece você não tem dori o bastante')
                    time.sleep(3)
                    diminição = Dori - 30
                    print(f'Pra o valor do machado você precisa de DR:{diminição}')
                    time.sleep(3)
                    print('\n') 

                print('\n')



    elif escolha == '3':
        print('=======================================')
        print('Convesar: ')
        print('=======================================')
        print('"Como você passou por lá?    "  = [1]')
        print('"Você sabe oque está por vim?"  = [2]')
        print('"Aonde encontrou as armas?   "  = [3]')
        print('=======================================')
        time.sleep(3)
        print('\n')

        while True:
            escolha = str(input('Oque quer perguntar? '))
            if escolha in '123':
                break
            print('')
            print('\033[31mERRO: Escolha uma das opções\033[m')
            time.sleep(1)
            print('')
            print('')
                
        if escolha == '1':
            if pagou == 'N' or pagou == '':
                if matando == 5:
                    print('Charlie: Quando você matou elas')
                    time.sleep(2)
                    print('Charlie: Eu só passei por lá')
                    time.sleep(2)
                    print('Charlie: Você fez algo que nimguem fez...')
                    time.sleep(2)
                    print('\n')

                else:      
                    print('Charlie: Simples hahaha')
                    time.sleep(2)
                    print('Charlie: Quando você ganhou da rainha')
                    time.sleep(2)
                    print('Charlie: Eu só passei por lá')
                    time.sleep(2)
                    print('Charlie: Dizendo que eu era da sua equipe')
                    time.sleep(3)
                    print('\n')
            
            elif pagou == 'sim':
                print('Charlie: Simples hahaha')
                time.sleep(2)
                print('Charlie: Quando você pagou a rainha')
                time.sleep(2)
                print('Charlie: Eu só passei por lá')
                time.sleep(2)
                print('Charlie: Dizendo que eu era da sua equipe')
                time.sleep(3)
                print('\n')

                
        elif escolha == '2':
            print('Charlie: Naverdade não')
            time.sleep(2)
            print('Charlie: Nunca passei por aqui')
            time.sleep(2)
            print('Charlie: Mais sei que não é coisa boa')
            time.sleep(3)
            print('\n')
                
        elif escolha == '3':
            print('Charlie: Encontrei com as pessoas da vila')
            time.sleep(2)
            print('Charlie: Estavam vendendo armas por lá ai eu comprei')
            time.sleep(2)
            print('Charlie: Pra vender pra pessoas como você')
            time.sleep(2)
            print('\n')
            

    elif escolha == '4':
        print('Charlie: Então ta certo amigo')
        time.sleep(2)
        print('Charlie: Boa sorte nesse novo caminho')
        time.sleep(2)
        print('Charlie: Não morra até lá em? Hahaha ')
        time.sleep(2)
        break
del intensB
intensB = intens[:]
print('\n')
print('\n')
print('\n')








print('O heroi encontrou o poço dos sonhos')
time.sleep(3)
print('O heroi ainda cansado descansa lá mesmo')
time.sleep(3)

if Nivel == 1:
    HP = 32
    mana = 60

elif Nivel == 2: 
    HP = 33
    mana = 70

elif Nivel == 3: 
    HP = 35
    mana = 80

elif Nivel == 4: 
    HP = 37
    mana = 90

elif Nivel == 5: 
    HP = 40
    mana = 100

elif Nivel == 6:
    HP = 40
    mana = 100

print('\033[32mHP MAX\033[m, \033[34mMANA MAX\033[m')
time.sleep(3)
print('\n')

print('\n')

print('O heroi se levanta')
time.sleep(2)
print('Dessa fez não está preso')
time.sleep(2)
print('Ele começa a andar')
time.sleep(2)
print('Não foi uma caminhada tão grande')
time.sleep(2)
print('Ele encontra 2 caminhos')
time.sleep(2)
print('\n')
















Dori = Dori2
while True:

    if Vivo == 'Sim ele está':
        if HP > 0:
            Vivo = ''
            break


    elif Morte > 0:
        Dori3 = Dori2
        Nivel = NivelB
        XP = XPB
        HP = 30
        if Nivel == 1:
            HP = 32
            mana = 60
            Nivel = 1

        elif Nivel == 2:
            HP = 33
            mana = 70
            Nivel = 2

        elif Nivel == 3: 
            HP = 35
            mana = 80

        elif Nivel == 4:
            HP = 37
            mana = 90

        elif Nivel == 5: 
            HP = 40
            mana = 100

        elif Nivel == 6:
            HP = 40
            mana = 100

        del intens
        intens = intensB[:]


        Morte = 0
        Mortes += 1



        print('Então o heroi morreu...')
        time.sleep(1)
        print(f'contagem de mortes = {Mortes}')
        time.sleep(2)
        print(f'Agora eu pergunto {nome} você que continuar? É uma pergunta de S ou N')
        time.sleep(1)

        while True:
            contiar = str(input('Resposta: ')).upper()
            if contiar in 'SsNn':
                break
            print('')
            print('Parece que você errou ou não a pergunta entendeu oque eu pedi')
            time.sleep(3)
            print('Digite de S ou N')
            time.sleep(1)
            print('')
            print('')


        if contiar == 'N':
            print('A que triste gostaria de continuar vendo essa historia')
            time.sleep(1)
            print(f'Então tchau {nome}')
            ACABAR += 1
            time.sleep(1)
            break


        elif contiar == 'S':
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('\n')
            print('\n')
            time.sleep(1)







    while True:
        print('No caminho da esquerda está um caminho feito de pedra')
        time.sleep(3)
        print('Como todos os outros')
        time.sleep(2)
        print('')

        print('No caminho da direita está um caminho que parece')
        time.sleep(3)
        print('Ser feito de carne e acido')
        time.sleep(2)
        print('')
        while True:
            escolha2 = str(input('Escolha umas das opções: [E/D]: '))
            if escolha2 in 'EDed':
                break
            print('')
            print('\033[31mERRO: escolha umas das opções\033[m')
            time.sleep(2)
            print('')
            print('')



        print('\n')
        print('\n')
        print('\n')        
        acer = ''
        if escolha2 in 'Ee':
            print('\n')
            print('O heroi vai até o caminho rochoso')
            time.sleep(2)
            print('Lá é bem quieto')
            time.sleep(2)
            print('Só tem pedra e mais pedra')
            time.sleep(2)
            print('Mais ele continua')
            time.sleep(2)
            print('')

            print('Encontrando uma rocha estranha')
            time.sleep(2)
            print('Parece ter se mexido')
            time.sleep(2)
            print('')

            while True:
                escolha = str(input('Quer atacar a rocha?: [S/N]: '))
                if escolha in 'SsNn':
                    break
                print('')
                print('\033[31mERRO: Escolha umas das opções\033[m')
                time.sleep(2)
                print('')
                print('')
            print('')

            if escolha in 'Ss':
                print('O heroi corre e da um ataque')
                time.sleep(2)
                print('Ela se reverá como um golem de pedra')
                time.sleep(3)

                print('\033[31m-5 de dano, no golem\033[m')
                time.sleep(2)
                acer = 'S'
                
            elif escolha in 'Nn':
                print('O heroi tenta passa reto mais')
                time.sleep(2)
                print('Era um golem de pedra!')
                time.sleep(2)
                print('O heroi tenta defender mais leva um soco dele')
                time.sleep(3)

                print('\033[31m-5 de dano\033[m')
                time.sleep(2)
                HP -= 5
                
            print('\n')
            hub(6)
            if HP <= 0:
                Morte += 1
                break
            print('\n')
            

            if matando == 5:
                print('O heroi matou o golem')
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\033[35mO poder aumentou\033[m')
                time.sleep(2)
                dori = random.randint(35, 40)
                Dori += dori
                print(f'\033[33mMais dori, DR:{Dori}\033[m')
                time.sleep(2)

            if Fugir == True:
                print('O heroi da seu ultimo ataque acabando a luta')
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\n')
                nivel()
                print('\n')
                print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
                print('')
                time.sleep(3)
                print('Com o golem morto o heroi vasculhou o corpo do golem')
                time.sleep(2)
                dori = random.randint(35, 40)
                Dori += dori
                print(f'\033[33mE encontra {dori} de dori! O dori está DR:{Dori}\033[m')
                time.sleep(3)
                Fugir = False
                print('')
                time.sleep(2)
                
            elif Fugir == 'A':
                print('O heroi fugiu da batalha...')
                time.sleep(2)
                Fugir = False
                print('Com isso não ganhou nada')
                time.sleep(2)

            print('\n')
            print('\n')
            print('\n') 
            print('\n')
            print('Depois de uma longa caminhada')
            time.sleep(3)
            print('O heroi encontra a luz do fim do caminho')
            time.sleep(3)
            print('Ele corre pra sair de lá, mais')
            time.sleep(2)
            print('Um pequeno colosso de pedra aparece')
            time.sleep(3)
            print('Ele é como um touro selvagem')
            time.sleep(2)
            print('')

            print('Ele se prepara e corre atrás do heroi')
            time.sleep(2)

            print('\n')
            hub(7)
            if HP <= 0:
                Morte += 1
                break
            print('\n')

            if matando == 5:
                print('O heroi matou o colosso')
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\033[35mO poder aumentou\033[m')
                time.sleep(2)                

            else:
                print('O heroi da seu ultimo ataque acabando a luta')
                time.sleep(2)
                xp = random.randint(210, 215)
                XP += xp
                print('\n')
                nivel()
                print('\n')
                print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
                print('')
                time.sleep(3)
                print('O pequeno colosso corre do heroi')
                time.sleep(2)
                print('O heroi não consegue alcançar ele')
                time.sleep(3)
                Fugir = False
                print('')
                time.sleep(2)
            
            print('\n')
            print('O heroi termina o caminho de pedra')
            time.sleep(2)
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            



        elif escolha2 in 'Dd':
            print('A carne te encomoda')
            time.sleep(2)
            print('É algo grudento e pegajoso')
            time.sleep(2)
            print('E o acido é sufocante')
            time.sleep(2)
            print('')

            print('Algo sai do acido')
            time.sleep(2)
            print('Uma coisa com muitos olhos')
            time.sleep(2)
            print('Feita de carne')
            time.sleep(2)
            print('')
            
            print('Ela vai em sua direção')
            time.sleep(2)
            print('Não tem outra opção a não ser lutar')
            time.sleep(3)

            print('\n')
            hub(8)
            if HP <= 0:
                Morte += 1
                break
            print('\n')

            if matando == 5:
                print('O heroi matou o monstro')
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\033[35mO poder aumentou\033[m')
                time.sleep(2)

            if Fugir == True:
                print('O monstro de carne foi morto')
                time.sleep(2)
                print('Ele parece está se mexendo ainda')
                time.sleep(2)
                print('O heroi da seu ultimo ataque acabando a luta')
                time.sleep(1)
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\n')
                nivel()
                print('\n')
                print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
                print('')
                time.sleep(3)
                Fugir = False
                print('')
            
            elif Fugir == 'A':
                print('O heroi fugiu da batalha...')
                time.sleep(2)
                Fugir = False
                print('Com isso não ganhou nada')
                time.sleep(2)


            print('\n')
            print('\n')
            print('\n')
            print('O caminho cada fez fica mais dificil de se passar')
            time.sleep(2)
            print('Tem muitos acidos no caminho')
            time.sleep(2)
            print('')


            print('A carne do chão e das paredes')
            time.sleep(2)
            print('ESTÃO SE MEXENDO!')
            time.sleep(2)
            print('E começa atacar o heroi!!!')
            time.sleep(2)
            print('\n')
            
            hub(9)
            if HP <= 0:
                Morte += 1
                break

            if matando == 5:
                print('O caminho fica quieto')
                time.sleep(2)
                print('\033[31mMATE ', end='', flush=True)
                time.sleep(2)
                print('MATE ', end='', flush=True)
                time.sleep(2)
                print('MATE\033[m', flush=True)
                time.sleep(2)
                print('O heroi começa atacar o caminho sem parar')
                time.sleep(3)
                print('Chegando ao ponto do caminho parar totalmente')
                time.sleep(4)
                print('O sufocamento parou')
                print('')
                time.sleep(2)
                xp = random.randint(200, 205)
                XP += xp
                print('\033[35mO poder aumentou\033[m')
                time.sleep(2)                

            else:
                print('O caminho ficou mais quieto')
                time.sleep(2)
                xp = random.randint(210, 215)
                XP += xp
                print('\n')
                nivel()
                print('\n')
                print(f'\033[35m{xp} A mais de poder, seu poder está {XP}\033[m')
                print('')
                time.sleep(3)
                Fugir = False
                print('')
                time.sleep(2)
            
            print('\n')
            print('Quando estava chegando ao final')
            time.sleep(2)
            print('O heroi encontra um esqueleto')
            time.sleep(2)
            print('Ele tem duas adagas vermelhas')
            time.sleep(2)
            print('')
            
            while True:
                escolha = str(input('Que pegar as adagas? [S/N]: '))
                if escolha in 'SsNn':
                    break
                print('')
                print('\033[31mERRO: Digite de S ou N\033[m')
                print('')
                print('')
            
            if escolha in 'Ss':
                print('')
                jogador.clear()
                jogador.append('Summoner')
                print('O heroi joga arma que está')
                time.sleep(2)
                print('E pega as adagas')
                time.sleep(2)
                print('Ele se sente como ja tivesse usado elas')
                time.sleep(2)
                print('')
            elif escolha in 'Nn':
                print('')
                print('O heroi passa reto do esqueleto')
                time.sleep(2)
                print('')
            
            print('\n')
            print('O heroi termina o caminho de carne')
            time.sleep(2)
            print('\n')
            print('\n')
            print('\n')
            print('\n')
        

        
        Vivo = 'Sim ele está'
        NivelB = Nivel
        XPB = XP
        del intensB
        intensB = intens[:]
        break


print('\n')
print('\n')
print('\n')
print('O heroi terminando o caminho')
time.sleep(2)
print('Encontra uma grande porta')
time.sleep(2)
print('Novamente...')
time.sleep(2)
print('\n')
print('\n')



cutcine = 0
print('O heroi encontrou o poço dos sonhos')
time.sleep(3)
print('O heroi ainda cansado descansa lá mesmo')
time.sleep(3)

if Nivel == 1:
    HP = 32
    mana = 60

elif Nivel == 2: 
    HP = 33
    mana = 70

elif Nivel == 3: 
    HP = 35
    mana = 80

elif Nivel == 4: 
    HP = 37
    mana = 90

elif Nivel == 5: 
    HP = 40
    mana = 100

elif Nivel == 6:
    HP = 40
    mana = 100

elif Nivel == 7:
    HP = 40
    mana = 100

elif Nivel == 8:
    HP = 45
    mana = 110

elif Nivel == 9:
    HP = 45
    mana = 110

elif Nivel == 10:
    HP = 45
    mana = 120

print('\033[32mHP MAX\033[m, \033[34mMANA MAX\033[m')
time.sleep(3)
print('\n')


print('Charlie não apareceu dessa vez')
time.sleep(2)
print('Tem nada a fazer')
time.sleep(2)
print('A não ser abrir a porta')
time.sleep(2)
print('')






Dori = Dori2
while True:

    if Vivo == 'Sim ele está':
        if HP > 0:
            Vivo = ''
            break


    elif Morte > 0:
        Dori3 = Dori2
        Nivel = NivelB
        XP = XPB
        HP = 30
        if Nivel == 1:
            HP = 32
            mana = 60
            Nivel = 1

        elif Nivel == 2:
            HP = 33
            mana = 70
            Nivel = 2

        elif Nivel == 3: 
            HP = 35
            mana = 80

        elif Nivel == 4:
            HP = 37
            mana = 90

        elif Nivel == 5: 
            HP = 40
            mana = 100

        elif Nivel == 6:
            HP = 40
            mana = 100
            
        elif Nivel == 7:
            HP = 40
            mana = 100

        elif Nivel == 8:
            HP = 45
            mana = 110

        elif Nivel == 9:
            HP = 45
            mana = 110

        elif Nivel == 10:
            HP = 45
            mana = 120

        del intens
        intens = intensB[:]


        Morte = 0
        Mortes += 1



        print('Então o heroi morreu...')
        time.sleep(1)
        print(f'contagem de mortes = {Mortes}')
        time.sleep(2)
        print(f'Agora eu pergunto {nome} você que continuar? É uma pergunta de S ou N')
        time.sleep(1)

        while True:
            contiar = str(input('Resposta: ')).upper()
            if contiar in 'SsNn':
                break
            print('')
            print('Parece que você errou ou não a pergunta entendeu oque eu pedi')
            time.sleep(3)
            print('Digite de S ou N')
            time.sleep(1)
            print('')
            print('')


        if contiar == 'N':
            print('A que triste gostaria de continuar vendo essa historia')
            time.sleep(1)
            print(f'Então tchau {nome}')
            ACABAR += 1
            time.sleep(1)
            break


        elif contiar == 'S':
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', end='', flush=True)
            time.sleep(1)
            print('.', flush=True)
            time.sleep(1)
            print('\n')
            print('\n')
            time.sleep(1)


    while True:









        while True:
            abrir = str(input('Aperte Enter/Enviar pra abrir a porta: '))
            if abrir == '':
                break
            print('')
            print('\033[31m ERRO: Aperte Enter/Enviar\033[m')
            print('')
            print('')
        print('\n')


        if cutcine == 0:
            print('Por algum motivo')
            time.sleep(2)
            print('Essa sala, tras pro heroi nostalgia')
            time.sleep(3)
            print('')

            print('*Barulho de serpente*')
            time.sleep(2)
            print('O heroi pega sua arma')
            time.sleep(2)
            print('*Mais barulho*')
            time.sleep(2)
            print('O heroi não encontra nada em sua volta')
            time.sleep(3)
            print('*Cada vez mais alto*')
            time.sleep(2)
            print('Mais quando olha pra cima')
            time.sleep(2)
            print('Uma grande serpente')
            time.sleep(2)
            print('Apreste a dar um bote')
            time.sleep(2)
            print('O heroi desvia do ataque')
            time.sleep(2)
            cutcine += 1
        
        elif cutcine == 1:
            print('A grande serpente aparece!')
            time.sleep(2)

        print('\n')
        hub(10)
        if HP <= 0:
            Morte += 1
            break
        print('\n')
        print('\n')
        print('\n')

        print('O serpente está ficando mais forte')
        time.sleep(2)
        print('Parece está se adaptando')
        time.sleep(2)
        print('')

        print('*GRITO*')
        time.sleep(2)
        print('<Desconhecido>: Ei deixa que eu te ajudo!')
        time.sleep(2)
        print('<Desconhecido>: Vai ser eu e você')
        time.sleep(2)
        print('*Parece ser uma elfa*')
        time.sleep(2)
        print('*Está usando um arco*')
        time.sleep(2)
        print('')
        print('Elfa: Usa essa poção')
        time.sleep(2)
        print('Elfa: Se não você vai morre')
        time.sleep(2)
        print('')

        print('\033[32mO heroi tomou a poção')
        time.sleep(2)
        if Nivel == 1:
            HP = 32
        elif Nivel == 2: 
            HP = 33
        elif Nivel == 3: 
            HP = 35
        elif Nivel == 4: 
            HP = 37
        elif Nivel == 5: 
            HP = 40
        elif Nivel == 6:
            HP = 40
        elif Nivel == 7:
            HP = 40
        elif Nivel == 8:
            HP = 45
        elif Nivel == 9:
            HP = 45
        elif Nivel == 10:
            HP = 45
        print('HP MAX\033[m')
        time.sleep(2)
        print('\n')



        hub(11)
        if HP <= 0:
            print('')
            print('Elfa: Não! Você levou muitos ataques')
            time.sleep(2)
            print('*O heroi não consegue ouvir direito*')
            time.sleep(2)
            print('Elfa: Calma eu vo-')
            time.sleep(2)
            Morte += 1
            print('\n')
            break
        print('\n')

        print('A serpente morreu')
        time.sleep(2)
        print('Elfa: Isso!')
        time.sleep(2)
        print('Elfa: Eu disse que eu ia ajudar!')
        time.sleep(2)
        print('')
        print('Elfa: Assim meu nome Nissan')
        time.sleep(2)
        print('Nissan: Agente podia fazer uma equipe')
        time.sleep(2)
        print('Nissan: Oque acha?')
        time.sleep(2)
        
        Vivo = 'Sim ele está'
        break


print('\n')
print('\n')
print('\n')
print('Capitulo 1 acabado')
time.sleep(5)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')



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

print('\n')
print('Assim eu tinha falado sobre um boss bonus')
time.sleep(2)
print('Vou fazer não KKKKKKKKKKKKKKKKKKKKKKKKK')
time.sleep(2)
print('Ou sim sei la')
