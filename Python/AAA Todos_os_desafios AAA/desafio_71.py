print('='*40)
print('banco ze pinto')
print('='*40)

valor = int(input('quanto quer sacar? R$'))

total = valor
ced = 50
tot = 0
totced = 0

while True:
    if total > ced:
        total -= ced
        tot += 1
        totced += 1
    else:
        if totced > 0:
            print(f'total de cedula {totced} de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break



