numero = int(0)
soma = int(0)
for somas in range(1, 7):
    pergunta = int(input(f'digite o valor {somas}: '))
    if numero % 2:
        soma += pergunta
        numero += 1
print(f'você informou {numero} numeros pares e a soma foi {soma}')
