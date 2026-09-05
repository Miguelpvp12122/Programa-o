import time

print('começando pograma...')
time.sleep(0.5)
print('carregando...')
time.sleep(0.5)
print('completo!')
time.sleep(0.5)
print('\n')

print('primeiro digite os 2 numeros. ')
numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
print('\n')
escolha = int(0)

while escolha != 'miguelpvp12122':
    print('=========⊱ menu do pograma ⊰=========')
    print('(1) somar os 2 numeros.')
    print('(2) multiplicar os 2 numeros.')
    print('(3) diminuir os 2 numeros.')
    print('(4) qual dos numeros é o maior.')
    print('(5) botar novos numeros.')
    print('(6) finalizar pograma.')
    print('\n')

    escolha = int(input('diga qual das opções quer selecionar: '))

    if escolha == 1:
        respostaS = numero1 + numero2
        print(f'A soma de {numero1} + {numero2} = {respostaS}')
        print('\n')
        time.sleep(2)

    elif escolha == 2:
        respostaM = numero1 * numero2
        print(f'a multiplicação de {numero1} X {numero2} = {respostaM}')
        print('\n')
        time.sleep(2)

    elif escolha == 3:
        respostaD = numero1 - numero2
        print(f'a diminuição dos numeros {numero1} - {numero2} = {respostaD}')
        print('\n')
        time.sleep(2)

    elif escolha == 4:
        if numero1 > numero2:
            maior = numero1
            print(f'entre o numero {numero1} e numero {numero2} o maior é {maior}')
        elif numero2 > numero1:
            maior = numero2
            print(f'entre o numero {numero1} e numero {numero2} o maior é {maior}')
        elif numero1 == numero2:
            print(f'o numero {numero1} e o numero {numero2} são iquais!')
        print('\n')
        time.sleep(2)

    elif escolha == 5:
        numero1 = int(input('digite novamente o primeiro numero: '))
        numero2 = int(input('digite agora o segundo numero: '))
        print('\n')
        time.sleep(2)

    elif escolha == 6:
        print('finalizando pograma...')
        time.sleep(4)
        print('\n')
        print('pograma finalizado.')
        break

    else:
        print('invalido por favor selecione uma das opções.')
        print('\n')
        time.sleep(2)
