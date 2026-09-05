soma = 0
for numero in range(0, 501 , 3):
    if numero % 3 == 0:
        soma = soma + numero
print(soma)