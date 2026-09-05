n = 1

tot = 1
num = 0
ZERO = 0

while ZERO != 999:
    n = int(input('digite um numero [999 para parar]: '))
    num = num + n
    tot += 1
    if n == 999:
        ZERO += 999
        num -= 999
print(f'a soma final de todos os numeros que foi digitado é {num}')