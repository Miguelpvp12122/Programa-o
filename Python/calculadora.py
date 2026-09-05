import time

tot = 0

time.sleep(0.5)
print('='*40)
print('começando pograma...')
time.sleep(0.5)
print('programa começado')
print('='*40)
print('\n')

print('='*40)
num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
print('='*40)
print('\n')
time.sleep(0.8)

print('='*40)
print('Calculadora Python')
print('='*40)
print('\n')
time.sleep(1)

while True:
    print('='*40)
    print('Menu do pograma:')
    print('(1) somar os 2 numeros')
    print('(2) diminuir os 2 numeros')
    print('(3) multiplicar os 2 numeros')
    print('(4) dividir os 2 numeros')
    print('(5) digitar novos numeros')
    print('(6) finalizar pograma')
    print('='*40)
    print('\n')

    print('='*40)
    time.sleep(0.5)
    escolha = int(input('escolha uma dessas opções: '))
    print('='*40)
    print('')

    if escolha == 1:
        time.sleep(0.5)
        print('\033[31m')
        print('='*40)
        soma = num1 + num2
        print(f'a soma entre o numero {num1} + {num2} = {soma}.')
        print('='*40)
        print('\033[m')
        print('\n')
        time.sleep(1)
        tot += 1

    elif escolha == 2:
        time.sleep(0.5)
        print('\033[31m')
        print('='*40)
        if num1 >= num2:
            menos = num1 - num2
            print(f'a diminuição de {num2} - {num1} = {menos}')
        elif num1 <= num2:
            menos = num2 - num1
            print(f'a diminuição de {num1} - {num2} = {menos}')
        print('='*40)
        print('\033[m')
        print('\n')
        time.sleep(1)
        tot += 1
    
    elif escolha == 3:
        time.sleep(0.5)
        print('\033[31m')
        print('='*40)
        multiplicação = num1 * num2
        print(f'a multiplicação de {num1} X {num2} = {multiplicação}')
        print('='*40)
        print('\033[m')
        print('\n')
        time.sleep(1)
        tot += 1
    
    elif escolha == 4:
        time.sleep(0.5)
        print('\033[31m')
        print('='*40)
        if num1 >= num2:
            divisão = num1 / num2
            print(f'a divisão de {num1} ÷ {num2} = {divisão}')
        elif num1 <= num2:
            divisão = num2 / num1
            print(f'a divisão de {num2} ÷ {num1} = {divisão}')
        print('='*40)
        print('\033[m')
        print('\n')
        time.sleep(1)
        tot += 1

    elif escolha == 5:
        time.sleep(0.5)
        print('='*40)
        num1 = int(input('digite seu novo primeiro numero: '))
        num2 = int(input('digite seu segundo novo numero: '))
        print('='*40)
        time.sleep(1)

    elif escolha == 6:
        print(f'você fez {tot} operações matematicas nesse pograma.')
        time.sleep(1)
        print('finalizando pograma...')
        time.sleep(1)
        print('pograma finalizado')
        time.sleep
        break
