tot2 = 0
import time
import random
classe = '1'
jogador = 'a'
ataqueI = 1

a= 'a'
if a == 'a':
    if a == 'a':
        if a == 'a':
            print('Qual das classes você desejaria escolher?')
            print('|Guerreiro|   [1]')
            print('|Arqueiro |   [2]')
            print('|Mago     |   [3]')
            time.sleep(1)
            print('\n')

            if tot2 == 0:
                print(
                    'OBS_1: Como Guerreiro como está perto do inimigo levara dano adicional e é uns que da mais dano')
                time.sleep(0.5)
                print(
                    'OBS_2: Como Arqueiro dara menos dano mais não receberar dano recebido a mais')
                time.sleep(0.5)
                print(
                    'OBS_3: Como Mago não levara dano adicional mais e da mais dano entre todo mais consome vida e mana')
                time.sleep
                tot2 += 1
                time.sleep(1)
                print('\n')

            while True:
                escolha = str(input('Quais das classes deseja escolher? '))
                if escolha in '123':
                    break
                print('')
                print('\033[31mERRO: Digite umas das opções\033[m')
                print('\n')
                print('')
                time.sleep(0.5)

            print('\n')

            if escolha == '1':
                jogador.clear()
                jogador.append('Guerreiro')

            elif escolha == '2':
                jogador.clear()
                jogador.append('Arqueiro')

            elif escolha == '3':
                jogador.clear()
                jogador.append('Mago')
            
            else:
                jogador.clear()
                jogador.append(random.choice(classe))

            print(
                f'Nova classe escolhida com sucesso! O heroi está com a classe {jogador[0]}')
            print('O heroi está atento aos ataques')
            print('Menos dano do inimigo')
            ataqueI -= 4
            time.sleep(1)
            print('\n')