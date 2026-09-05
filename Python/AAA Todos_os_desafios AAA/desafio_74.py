import random

tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

for t in tupla:
    print(t , end=' ')


print(f'\n')
print(f'o maior numero foi {max(tupla)}')
print(f'menor numero foi {min(tupla)}')