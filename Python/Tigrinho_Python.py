import random
import time

Tot = 0
TotP = 0
TotN = 0

Saldo = 10.0

print('=== Tigrinho Python ===')
time.sleep(1)
print('\n')

while True:
    print(f'Seu saldo é de R$: {Saldo:.2f} reais')
    time.sleep(1)
    print('')

    while True:
        pergunta = float(input('Quantos reais que aposta? '))
        if pergunta <= Saldo:
            break
        print('')
        print('\033[31mERRO DIGITE ENTRE UM NUMERO MENOR OU IQUAL AO SALDO\033[m')
        time.sleep(2)
        print('')
        print('')

    Saldo -= pergunta
    print('')

    num1 = random.randint(1, 7)
    print(num1, end=' ', flush=True)
    time.sleep(0.5)
    num2 = random.randint(1, 7)
    print(num2, end=' ', flush=True)
    time.sleep(0.5)
    num3 = random.randint(1, 7)
    print(num3, end=' ', flush=True)
    time.sleep(0.5)
    print('')

    numero = num1 + num2 + num3

    time.sleep(1)
    print('')
    if numero <= 9:
        print('\033[31mVocê perdeu todo o dinheiro apostado\033[m')
        pergunta -= pergunta
        Saldo += pergunta
        TotN += 1

    elif numero <= 12 and numero > 9:
        print('\033[31mVocê perdeu a metade do dinheiro apostado\033[m')
        pergunta /= 2
        Saldo += pergunta
        TotN += 1

    elif numero > 12 and numero < 20:
        print('\033[32mVocê multiplicou 1.5 porcento doque apostou!\033[m')
        pergunta *= 1.5
        Saldo += pergunta
        TotP += 1

    else:
        print('\033[32mVocê multiplicou 2.0 vezes o dinheiro apostado!!!\033[m')
        pergunta *= 2
        Saldo += pergunta
        TotP += 1


    Tot += 1

    print('\n')
    time.sleep(1)

    if TotN == 10:
        print('Você teve muitas vezes de azar')
        time.sleep(1)
        break

    if TotP == 10:
        print('Você já teve muitas sortes')
        time.sleep(1)
        break

    if Tot == 15:
        print('Você apostou muitas vezes')
        time.sleep(1)
        break

    if Saldo < 0:
        Saldo = 0

    if Saldo < 1:
        print('Saldo acabado')
        time.sleep(1)
        break

    while True:
        Continuar = str(input('Você deseja continuar? [S/N]: '))
        if Continuar in 'SNsn':
            break
        print('')
        print('\033[31mERRO DIGITE ENTRE S ou N\033[m')
        time.sleep(0.5)
        print('')
        print('')


    if Continuar == 'N' or Continuar == 'n':
        break

    print('\n')
    print('\n')
    print('\n')
    time.sleep(1)


print('\n')
print('\n')
time.sleep(2)

print(f'Seu saldo no final foi de R$: {Saldo:.2f}')

time.sleep(2)

print(f'Apostou exatamente {Tot} vezes')

time.sleep(2)

print(f'Teve {TotP} vezes de sorte e teve {TotN} vezes de azar')
