maior = 0
menor = 0
for pesos in range(1,5):
    pessoas = float(input(f'diga o pessoa da {pesos}: '))
    if pesos == 1:
        maior = pessoas
        menor = pessoas
    else:
        if pesos > maior:
            maior = pesos
        elif pesos < menor:
            menor = pesos

print(f'o maior peso é {maior} o menor peso é {menor}')
