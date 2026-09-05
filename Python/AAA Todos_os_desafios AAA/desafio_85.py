PI = [[] , []]
dados = list()

tot = 0

for R in range(0, 7):
    tot += 1
    dados.append(int(input(f'digite o {tot}ª numero: ')))

    divisão = dados[0] % 2

    if divisão == 0:
        PI[0].append(dados[0])
    else:
        PI[1].append(dados[0])

    dados.clear()

print('\n')
print('os numeros pares foi ', end='')
for p in PI[0]:
    print(f' {p}, ', end='')
print('\n')

print('os numeros impares foi ', end='')
for i in PI[1]:
    print(f'{i}, ', end='')