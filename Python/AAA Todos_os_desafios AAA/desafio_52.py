numero = int(input('digite um numero: '))
tot = int(0)
for C in range(1, numero + 1, 1):
    if numero % C == 0:
        tot += 1
if tot == 2:
    print('ele é um numero primo')
else:
    print('ele não é')