km = int(input('quantos quilometros voce percoreu? '))


if km >200:
    print('agora seus km vai esta R$15 a menos pos passou dos 200km ')
    percorrendo = (km*0.45)
    print(f'voce vai precisar pagar R$:{percorrendo} ')
    print('tenha um bom dia!')
else:
    percorrendo2 = (km*0.50)
    print(f'você precisa pagar so {percorrendo2}')
    print('tenha um bom dia')
