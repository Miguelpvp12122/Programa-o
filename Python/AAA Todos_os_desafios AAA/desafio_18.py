import random
a1 = str(input('digite o nome do primeiro aluno: '))
a2 = str(input('digite o segundo: '))
a3 = str(input('digite o terceiro: '))
a4 = str(input('digite o quarto: '))

lista = [a1, a2, a3, a4]

random = random.shuffle (lista)

print(f'a ordem que os alunos que vao fazer o trabalho é  ')
print(f'{lista}')