a = input('qual o primeiro numero? ') 
b = input('qual o segundo? ')
c = input('e o terceiro? ')
menor = a 
if b<a and b>c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b >c:
    maior = b
if c > a and c > b:
    maior = c
print(f'o menor valor digitado é {menor}')
print(f'o maior foi {maior}')