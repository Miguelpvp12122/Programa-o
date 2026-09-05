maior = 0
menor = 0

lista = list()
for l in range(0, 5):
    lista.append(int(input('digite um numero: ')))
    if l == 0:
        maior = menor = lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        
        elif lista[l] < menor:
            menor = lista[l]

print(f'o maior numero foi {maior}')
for v, i in enumerate(lista):
    if i == maior:
        print(f'na posição  {v +1}')

print(f'o menor numero foi {menor}')
for b, o in enumerate(lista):
    if o == menor:
        print(f'o menor numero foi {b}')