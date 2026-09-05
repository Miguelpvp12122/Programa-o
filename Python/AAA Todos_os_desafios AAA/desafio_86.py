x3 = [[], [], []]
dados = list()

tot1 = 0
tot2 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    x3[0].append(dados[:])
    dados.clear()

#    print(x3)

tot1 += 1
tot2 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    x3[1].append(dados[:])
    dados.clear()
    
#    print(x3)

tot1 += 1
tot2 = 0

for p in range(0, 3):
    dados.append(int(input(f'digite um numero pra [{tot1}][{tot2}]: ')))
    tot2 += 1

    x3[2].append(dados[:])
    dados.clear()
    
#    print(x3)

for p in range(0,1):
    print(f'[ {x3[0][0]} ] [ {x3[0][1]} ] [  {x3[0][2]} ]')
    print(f'[ {x3[1][0]} ] [ {x3[1][1]} ] [  {x3[1][2]} ]')
    print(f'[ {x3[2][0]} ] [ {x3[2][1]} ] [  {x3[2][2]} ]')

