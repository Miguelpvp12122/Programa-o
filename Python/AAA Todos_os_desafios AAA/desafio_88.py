from random import randint

lista = list()
jogos = list()

tot2 = 1

print('=='*30)
print('jogo da mega cena')
print('=='*30)
quantidade = int(input('quantos jogos quer que eu sorteie? '))

while tot2 <= quantidade:
    tot = 0
    while True:
        num = randint(1, 60)

        if num not in lista:
            tot += 1
            lista.append(num)
        
        if tot >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()

    tot2 += 1

for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

