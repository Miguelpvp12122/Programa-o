lista = list() # ou pode ser so o (  lista = []  )

for a in range(1, 5):
    lista.append(int(input('digite um numero: ')))

for v, l in enumerate(lista):
    print(f'no valor {v +1} eu encontrei o valor {l}')
print('FIM')