import desafio_108M
valor = int(input('quanto de dinheiro você tem? '))
print(f'a metade de {desafio_108M.moeda(valor)} é {desafio_108M.moeda(desafio_108M.metade(valor))}')
print(f'o dobro de {desafio_108M.moeda(valor)} é {desafio_108M.moeda(desafio_108M.dobro(valor))}')
print(f'10% a mais de {desafio_108M.moeda(valor)} é {desafio_108M.moeda(desafio_108M.aumentar(valor, 10))}')
print(f'13% a menos de {desafio_108M.moeda(valor)} é {desafio_108M.moeda(desafio_108M.diminuir(valor, 13))}')
