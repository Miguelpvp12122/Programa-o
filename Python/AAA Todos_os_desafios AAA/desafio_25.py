frase = input('digite um frase/palavra aqui: ')

quantos_a = frase.count('a')

onde_começa = frase.find('a')

onde_fim = frase.rfind('a')

print(f'sua frase/palavra tem {quantos_a} letras')
print(f'o primeiro a aparece na pocição {onde_começa+1}')
print(f'e ela termina na pocisão {onde_fim+1}')