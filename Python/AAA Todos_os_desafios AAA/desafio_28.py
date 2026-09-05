km = float(input('quantos km voce estava percorrendo por hora? '))
if km >80:
    print(f'voce foi multado! ')
    multa = (km-80) * 7
    print(f'sua multa foi de {multa:.2f}')

else:
    print('voce estava na velocidade certa obrigado!')