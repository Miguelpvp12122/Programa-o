valor = float(input('qual o valor do seu produto? '))
paga = str(input('vai pagar cartão ou dinheiro? '))
vista = input('vai pagar a vista? (sim ou nâo) ')

if paga == 'dinheiro' and vista == 'sim':
    total = (valor*10/100)
    valor -= total
    print(f'você ganhou desconto de 10% o seu produto está R$:{valor} .') 
elif paga == 'dinheiro' and vista == 'não':
    print('o valor vai ser o normal.')
elif paga == 'cartão' and vista == 'sim':
    total2 = (valor*5/100)
    valor -= total2
    print(f'você ganhou 5% de desconto o seu produto está R$:{valor} .')
elif paga == 'cartão' and vista == 'não':
    vezes = input('quer pagar por quantas vezes? X ')
    if vezes == '2':
        valor /= 2
        print(f'em 2 messes você precisa pagar um valor de {valor}')
    elif vezes == '3':
        valor /= 3
        print(f'em 3 messes você precisa pagar o valor de {valor} ')