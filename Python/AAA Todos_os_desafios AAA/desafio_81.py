lista = list()
tot = 0

while True:
    lista.append(int(input('digite um numero: ')))
    tot += 1
    continuar = str(input('quer continuar? [S/N]: '))
    
    
    if continuar == 'N':
        break

lista.sort(reverse = True)
print(f'você digitou {tot} numeros')
print(f'a ordem decressente é {lista}')
if 5 in lista:
    print('existe o valor cinco na lista! ')
else:
    print('não existe o valor cinco na lista.')