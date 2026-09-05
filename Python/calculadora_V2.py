from time import sleep


num = 0

while True:
    print('============================')
    print('\033[36m [+]        = soma')
    print(' [-]        = subtração')
    print(' [/] or [÷] = divisão')
    print(' [*] or [x] = multiplicação\033[m')
    print('============================')


    if num == 0:
        while True:
            try:
                num = float(input('Numero:    '))

            except (ValueError, KeyError):
                print('')
                print('\033[31mERRO: Digite um numero valido!\033[m')
                sleep(0.5)
                print('\n')

            else:
                break
    elif num > 0:
        print(f'Numero:    {num}')
    
    while True:
        escolha = str(input('Sinal:     '))
        if escolha in '+-/÷*Xx':
            break
        print('')
        print('\033[31mERRO: Digite alguns dos sinais a cima\033[m')
        sleep(0.5)
        print('\n')

    while True:
        try:
            num2 = float(input('Numero 2:  '))
        
        except (ValueError, KeyError):
            print('')
            print('\033[31mERRO: Digite um numero valido!\033[m')
            sleep(0.5)
            print('\n')
        
        else:
            break
    
    sleep(1)



    if escolha == '+':
        num3 = num + num2
        print(f'A soma entre {num} + {num2} = {num3}')
        sleep(0.5)

    if escolha == '-':
        if num >= num2:
            num3 = num - num2
            print(f'A subtração de {num} - {num2} = {num3}')
        if num2 > num:
            num3 = num2 - num
            print(f'A subtração de {num2} - {num} = {num3}')
            sleep(0.5)

    if escolha == '/' or escolha == '÷':
        try:
            if num >= num2:
                num3 = num / num2
                print(f'A divisão de {num} ÷ {num2} = {num3}')
                sleep(0.5)
            if num2 > num:
                num3 = num2 / num
                print(f'A subtração de {num2} ÷ {num} = {num3}')
                sleep(0.5)
        
        except ZeroDivisionError:
            print('')
            print('\033[31mERRO: Zero não pode ser divido por um numero\033[m')
            print('\n')
            sleep(0.5)
            num3 = 0

    if escolha == '*' or escolha == 'X' or escolha == 'x':
        num3 = num * num2
        print(f'A multiplicação de {num} X {num2} = {num3}')
        sleep(0.5)


    print('\n')
    while True:
        ficar = str(input('Deseja continuar com o resultado? [S/N]: '))
        if ficar == 'S' or ficar == 's':
            num = num3
            break
        elif ficar == 'N' or ficar == 'n':
            num = 0
            break
        print('')
        print('\033[31mERRO: Digite entre S or N\033[m')
        print('\n')
        sleep(0.5)


    print('\n')
    sleep(0.5)
