maior = menor = cont = mil = ZERO = 0
barato = ''

print('='*40)
print('mercado do ze pinto')
print('='*40)
print('\n')

while True:
    print('='*40)
    Nproduto = str(input('qual o nome do produto? '))
    Pproduto = float(input(f'qual o preço da {Nproduto}? '))
    print('='*40)

    cont += 1

    pergunta = str(input('quer continuar? [N/S]: '))

    ZERO += Pproduto

    if cont == 1:
        menor = Pproduto
        barato = Nproduto
    else:
        if Pproduto < menor:
            Pproduto = menor
            barato = Nproduto

    if Pproduto > 1000:
        mil += 1
    
    if pergunta == 'N':
        break

print(f'a soma dos {cont} produto(s) é R${ZERO} ')
print(f'temos {mil} produto(s) maior doque R$1000')
print(f'o produto mais barato foi {menor} o nome dele é {barato}')
