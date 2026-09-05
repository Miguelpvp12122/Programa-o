import datetime

dados = {}

dados['nome'] = str(input('digite seu nome: '))

data = int(input('qual a sua data? '))
dados['idade'] = data - datetime.datetime.now().year

dados['CLT'] = int(input('digite o CLT: [0 não tem]: '))
if dados['CLT'] == 0:
    print('')
else:
    dados['contra'] = int(input('ano da contratação: '))

    dados['salario'] = float(input('salario: R$'))

    dados['aponse'] = dados['idade'] + (dados['contra'] + 35) - datetime.datetime.now().year

print('=='* 30)
for i, v in dados.items():
    print(f'  - {i} tem o valor {v}')
