import time

cadrastosN = []
cadrastosA = []
tot = 0

while True:
    print('==============================')
    print('        MENU PRINCIPAL')
    print('==============================')
    time.sleep(0.5)
    print('')
    print('________________________________________')
    print('\033[34m[1]    Ver lista de cadrastos')
    print('[2]    Adicionar mais uma pessoa')
    print('[3]    Sair do pograma\033[m')
    print('________________________________________')
    print('\n')
    time.sleep(0.5)

    while True:
        try:
            escolha = int(input('\033[36mDigite umas das opções: \033[m'))
            print('\n')
        

        except:
            print('')
            print('\033[31mERRO: Digite uma das opções!\033[m')
            time.sleep(1)
            print('\n')

        else:
            try:
                if escolha == 1:
                    print('============================================')
                    print('        Todas as pessoas cadrastadas')
                    print('============================================')
                    for p in cadrastosN:
                        time.sleep(0.5)
                        print(f'Nome:{cadrastosN[tot]}           Idade:{cadrastosA[tot]} ')
                        tot += 1
                    print('\n')
                



                if escolha == 2:
                    print('========================')
                    print('        CADRASTO')
                    print('========================')
                    
                    nome = str(input('Digite o nome: '))

                    while True:
                        try:
                            idade = int(input('Digite a idade: '))
                        
                        except:
                            print('')
                            print('\033[31mERRO: Digite um numero inteiro\033[m')
                            time.sleep(1)
                            print('\n')

                        else:
                            cadrastosA.append(idade)
                            break

                    cadrastosN.append(nome)
                    print(f'Cadradratado(a) com sucesso')
                    time.sleep(1)
                    print('\n')
                



                if escolha == 3:
                    print(f'Até logo tenha um otimo dia :D')
                    break
            
            except:
                print('')
                print('ERRO: Escolha umas das opções')
                time.sleep(1)
                print('\n')
            if escolha in (1, 2, 3):
                print()
            else:
                print('')
                print('\033[31mERRO: Escolha umas das opções\033[m')
                time.sleep(1)
                print('\n')

            break
