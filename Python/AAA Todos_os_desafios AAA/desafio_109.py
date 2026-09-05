import desafio_109M
valor = int(input('quanto de dinheiro você tem? '))
print(f'a metade de {desafio_109M.moeda(valor)} é {desafio_109M.metade(valor, True)}')

print(f'o dobro de {desafio_109M.moeda(valor)} é {desafio_109M.dobro(valor, True)}')

print(f'10% a mais de {desafio_109M.moeda(valor)} é {desafio_109M.aumentar(valor, 10, True)}')

print(f'13% a menos de {desafio_109M.moeda(valor)} é {desafio_109M.diminuir(valor, 13, True)}')
