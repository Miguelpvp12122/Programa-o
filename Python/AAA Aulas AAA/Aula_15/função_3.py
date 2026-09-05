def dobra(lst):
    tot = 0
    while tot < len(lst):
        lst[tot] *= 2
        tot += 1

lista = [3, 10, 70]
dobra(lista)
print(lista)
