per = (('digite um numero: '))

tot = 0

cont = 0

maior = 0

menor = 0

while per not in 'nN':
    n = int(input('digite um numero: '))
    per = str(input('você quer continuar? [S, N]: '))
    tot += n
    cont += 1

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < maior:
            menor = n

media = tot / cont
print(f'a soma entre todos os numeros é {tot}, você digitou {cont} vezes, a media dos numeros digitados é {media}, o maior numero foi {maior} e o menor foi {menor} ')