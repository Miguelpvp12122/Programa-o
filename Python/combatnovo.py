import time
import random

jazzghost = 30
HP = 40
mana = 100

tot1 = tot2 = 0

intens = ['Poção pequena', 'Poção media  ', 'Poção grande ', 'Poção de mana']
classe = ['Guerreiro', 'Arqueiro', 'Mago']
escolhe = random.choice(classe)
jogador = []
jogador.append(escolhe)


while True:
    ataque1 = random.randint(3, 4)
    ataque2 = random.randint(7, 8)
    ataque3 = random.randint(1, 12)

    sangue = random.randint(1, 4)

    ataqueI = random.randint(8, 9)

    print(f'você está com a classe {jogador}')
    print('\n')

    print('='*40)
    print('hub de opções:')
    print('='*40)
    print('|Atacar| [1]')
    print('|Itens | [2]')
    print('|classe| [3]')
    print('|Fugir | [4]')
    print('='*40)
    time.sleep(1)
    print('\n')

    hub = int(input('digite umas das opções: '))
    time.sleep(1)
    print('\n')

    if hub == 1:
        if jogador ==  ['Guerreiro']:

            ataque1 = random.randint(5, 6)
            ataque2 = random.randint(8, 10)
            ataque3 = random.randint(1, 16)

            print('='*40)
            print('hub de ataque:')
            print('='*40)
            print('|ataque rapido| = 5/6 de dano:     [1]')
            print('|ataque pesado| = 8/10 de dano:     [2]')
            print('|tudo ou nada!| = 1 a 16 de dano:  [3]')
            print('='*40)
            time.sleep(1)
            print('\n')

            
            escolha = int(input('escolha um ataque: '))
            print('\n')

            if escolha == 1:
                jazzghost -= ataque1
                print(f'\033[31mo heroi correu e deu um ataque fraco , -{ataque1} de dano \033[m, jazzghost ficou com {jazzghost} de sua vida')
                ataqueI += 1
                time.sleep(1)
                print('\n')

            elif escolha == 2:
                jazzghost -= ataque2
                print(f'\033[31mo heroi de um pulo e deu um ataque pra baixo em jazzghost, -{ataque2} de dano \033[m,jazzghost ficou com {jazzghost} de sua vida ')
                print('você fez o ataque e ficou esposto a um ataque mais forte.')
                ataqueI += 2
                time.sleep(1)
                print('\n')

            elif escolha == 3:
                jazzghost -= ataque3
                HP -= sangue
                print(f'\033[31mtudo ou nada!!! o heroi usa uma magia com seu sangue em sua espada e vai em dando um corte em jazzghost, o heroi perde sangue ele leva -{sangue} de dano o HP está {HP}, -{ataque3} de dano \033[m, jazzghost ele está com {jazzghost} de vida')
                time.sleep(1)
                print('\n')

        elif jogador == ['Arqueiro']:

            ataque1 = random.randint(4, 5)
            ataque2 = random.randint(7, 8)
            ataque3 = 10

            print('='*50)
            print('hub de ataque:')
            print('='*50)
            print('|tiros consecutivos| = 4/5 de dano:     [1]')
            print('|tiro certeiro     | = 7/8 de dano:     [2]')
            print('|tiro magico       | = 10 de dano:      [3]')
            print('='*50)
            time.sleep(1)
            print('\n')

            
            escolha = int(input('escolha um ataque: '))
            print('\n')

            if escolha == 1:
                jazzghost -= ataque1
                print(f'\033[31mo heroi deu tiros no jazzghost, -{ataque1} de dano \033[m, jazzghost ficou com {jazzghost} de sua vida')
                time.sleep(1)
                print('\n')

            elif escolha == 2:
                jazzghost -= ataque2
                print(f'\033[31mo heroi segura seu arco com força e da um tiro certeiro, -{ataque2} de dano \033[m,jazzghost ficou com {jazzghost} de sua vida ')
                ataqueI += 1
                time.sleep(1)
                print('\n')

            elif escolha == 3:
                if mana >= 20:
                    jazzghost -= ataque3
                    mana -= 20
                    print(f'\033[31mo heroi uma magia em seu arco e atira contra o jazzghost, -{ataque3} de dano \033[m, jazzghost ele está com {jazzghost} de vida')
                    print(f'\033[34mvocê usou mana! menos 20 de mana, sua mana está {mana}\033[m')
                    time.sleep(1)
                    print('\n')
                else:
                    print('você não tem mana o suficiente pra executar o ataque')
                    ataqueI -= 3
                    time.sleep(1)
                    print('\n')



        elif jogador == ['Mago']:
            ataque1 = random.randint(5, 7)
            ataque2 = random.randint(8, 10)
            ataque3 = random.randint(10, 13)

            print('='*50)
            print('hub de ataque:')
            print('='*50)
            print('|em chamas!    | = 5/7 de dano:     [1]')
            print('|absorva       | = 8/10 de dano:    [2]')
            print('|pacto de sague| = 10/15 de dano:   [3]')
            print('='*50)
            time.sleep(1)
            print('\n')

            
            escolha = int(input('escolha um ataque: '))
            print('\n')

            if escolha == 1:
                if mana >= 10:
                    jazzghost -= ataque1
                    mana -= 10
                    print(f'\033[31mo heroi faz uma magia e queima o jazzghost, -{ataque1} de dano \033[m, jazzghost ficou com {jazzghost} de sua vida')
                    print(f'\033[34mvocê usou mana! menos 10, sua mana está {mana}\033[m')
                    time.sleep(1)
                    print('\n')
                else:
                    print('você não tem mana o suficiente pra executar o ataque')
                    ataqueI -= 3
                    time.sleep(1)
                    print('\n')

            elif escolha == 2:
                if mana >= 15:
                    jazzghost -= ataque2
                    mana += 15
                    print(f'\033[31mo heroi faz uma magia e absorve o jazzghost pras sombras, -{ataque2} de dano \033[m,jazzghost ficou com {jazzghost} de sua vida ')
                    print(f'\033[34mvocê usou mana! menos 15, sua mana está {mana}\033[31m')
                    time.sleep(1)
                    print('\n')
                else:
                    print('você não tem mana o suficiente pra executar o ataque')
                    ataqueI -= 3
                    time.sleep(1)
                    print('\n')

            elif escolha == 3:
                if mana >= 25:
                    sangue -= 1
                    HP -= sangue
                    jazzghost -= ataque3
                    print(f'\033[31mo heroi usa de um pacto pra apricar o ataque no jazzghost usando do seu sangue, -{ataque3} de dano \033[m, jazzghost ele está com {jazzghost} de vida')
                    print(f'você usou do seu sangue e mana! \033[34mmenos 25 de mana\033[m e menos \033[31m-{sangue} de vida\033[m')
                    time.sleep(1)
                    print('\n')
                else:
                    print('você não tem mana o suficiente pra executar o ataque')
                    ataqueI -= 3
                    time.sleep(1)
                    print('\n')
            

    if hub == 2:
        print('='*40)
        print('hub de itens: ')
        print('='*40)
        print('seus intens:')
        for n in intens:
            tot1 += 1
            print(f'|{n}|            [{tot1}]')
        print('='*40)
        tot1 -= 4
        time.sleep
        print('\n')

        escolha = int(input('escolha um item: '))

        if escolha == 1:
            if intens[0] == 'Poção pequena':
                HP += 6
                print(f'\033[32mvocê tomou uma poção pequena seu HP está {HP}\033[m')
                del intens[0]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[0] == 'Poção media  ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção media seu HP está {HP}\033[m')
                del intens[0]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[0] == 'Poção grande ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção grande seu HP está {HP}\033[m')
                del intens[0]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[0] == 'Poção de mana':
                mana += 150
                print(f'\033[34mvocê tomou poção de mana sua mana está {mana}\033[m')
                del intens[0]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[0] == '             ':
                print(f'nenhum intem encontrada')
                time.sleep(1)
                print('\n')

        elif escolha == 2:
            if intens[1] == 'Poção pequena':
                HP += 6
                print(f'\033[32mvocê tomou uma poção pequena seu HP está {HP}\033[m')
                del intens[1]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[1] == 'Poção media  ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção media seu HP está {HP}\033[m')
                del intens[1]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[1] == 'Poção grande ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção grande seu HP está {HP}\033[m')
                del intens[1]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[1] == 'Poção de mana':
                mana += 150
                print(f'\033[34mvocê tomou poção de mana sua mana está {mana}\033[m')
                del intens[1]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[1] == '             ':
                print(f'nenhum intem encontrada')
                time.sleep(1)
                print('\n')

        elif escolha == 3:
            if intens[2] == 'Poção pequena':
                HP += 6
                print(f'\033[32mvocê tomou uma poção pequena seu HP está {HP}\033[m')
                del intens[2]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[2] == 'Poção media  ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção media seu HP está {HP}\033[m')
                del intens[2]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[2] == 'Poção grande ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção grande seu HP está {HP}\033[m')
                del intens[2]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[2] == 'Poção de mana':
                mana += 150
                print(f'\033[34mvocê tomou poção de mana sua mana está {mana}\033[m')
                del intens[2]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[2] == '             ':
                print(f'nenhum intem encontrada')
                time.sleep(1)
                print('\n')

        if escolha == 4:
            if intens[3] == 'Poção pequena':
                HP += 6
                print(f'\033[32mvocê tomou uma poção pequena seu HP está {HP}\033[m')
                del intens[3]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[3] == 'Poção media  ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção media seu HP está {HP}\033[m')
                del intens[3]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[3] == 'Poção grande ':
                HP += 10
                print(f'\033[32mvocê tomou uma poção grande seu HP está {HP}\033[m')
                del intens[3]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[3] == 'Poção de mana':
                mana += 150
                print(f'\033[34mvocê tomou poção de mana sua mana está {mana}\033[m')
                del intens[3]
                intens.append('             ')
                ataqueI -= 3
                time.sleep(1)
                print('\n')
            elif intens[3] == '             ':
                print(f'nenhum intem encontrada')
                time.sleep(1)
                print('\n')



    elif hub == 3:
        print('qual das classes você deseja escolher?')
        print('|Guerreiro|   [1]')
        print('|Arqueiro |   [2]')
        print('|Mago     |   [3]')
        time.sleep(1)
        print('\n')

        if tot2 == 0:
            print('OBS_1: como Guerreiro como está perto do inimigo levara dano adicional e é uns que da mais dano')
            print('OBS_2: como Arqueiro dara menos dano mais não receberar dano recebido a mais')
            print('OBS_3: como Mago não levara dano adicional mais e da mais dano entre todo mais consome vida e mana')
            tot2 += 1
            time.sleep(1)
            print('\n')

        escolha = int(input('qual das classes você escolhe? '))
        print('\n')

        if escolha == 1:
            jogador.clear()
            jogador.append('Guerreiro')
        
        elif escolha == 2:
            jogador.clear()
            jogador.append('Arqueiro')

        elif escolha == 3:
            jogador.clear()
            jogador.append('Mago')

        print(f'nova classe escolhida com sucesso! você está como {jogador}')
        print('você está atento aos ataques')
        print('menos dano do inimigo')
        ataqueI -= 5
        time.sleep(1)
        print('\n')





    elif hub == 4:
        print('você tenta corre mais não consegue!')
        print('\033[37mjazzghost bloqueia o caminho.\033[m')
        time.sleep(1)
        print('\n')


    if jazzghost <= 0:
        print('o heroi ganha do jazzghost.')
        time.sleep(1)
        print('demo acabada!')
        break

    
    print('hora do jazzghost atacar!')
    HP -= ataqueI
    print(f'\033[31mjazzghost usa um jegue no heroi e da -{ataqueI}, o heroi está com {HP} de hp \033[m')
    time.sleep(1)
    print('\n')

    if HP <= 0:
        print('\033[31mheroi morreu.')
        time.sleep(1)
        print('TENHA DETERMINAÇÃO NÃO DESISTA!!!')
        time.sleep(0.5)
        print('até logo heroi...')
        break

    if jazzghost <= 0:
        print('o heroi ganha do jazzghost.')
        time.sleep(1)
        print('demo acabada!')
        break
