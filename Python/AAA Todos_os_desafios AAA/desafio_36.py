casa = float(input('valor da casa: R$'))
salario = float(input('salario do comprador: R$'))
anos = float(input('quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar a casa de {casa} em {anos}')
print(f'a prestaçao vai ser de {prestaçao}')
if prestaçao <= minimo:
    print('CONSEDIDO')
else:
    print('RECUSADO')
