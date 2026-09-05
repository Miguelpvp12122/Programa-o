lista = ['pão', 'amendoim', 'chocolate']

lista.pop() # retira o ultimo numero, em dentro da aspa pode expecivicar qual quer ser deletado

print(lista)

del lista[0]

print(lista)

lista = ['pão', 'amendoim', 'chocolate']

if 'pão' in lista:
    lista.remove('amendoim') # remove oque está sendo expecivicado
else:
    print('não encontrei oque está sendo expecivicado') # se não for encontrado da erro

print(lista)


