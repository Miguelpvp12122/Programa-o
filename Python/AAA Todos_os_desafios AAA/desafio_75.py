numeros = (int(input('digite um numero: ')), int(input('digite outro numero: ')),
           int(input('digite mais um numero: ')),   int(input('digite o ultimo numero: ')))

print(f'você digitou os valores {numeros}')


print(f'o numero nove apareceu {numeros.count(9)}')

if 3 in numeros:
    print(f'o primeiro três apareceu na posição {numeros.index(3)+1}ª')
else:
    print('o três não aparece nenhuma fez')

print('os valores pares digitados foram ', end='')
for n in numeros:
    print( n, end=' ' )
    if n % 2 == 0:
        print(n , end=' ')