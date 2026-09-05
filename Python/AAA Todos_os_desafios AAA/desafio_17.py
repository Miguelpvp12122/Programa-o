import random
a1 = str(input('qual o nome do primeiro aluno? '))
a2 = str(input('qual o nome do segundoaluno? '))
a3 = str(input('qual o do terceiro? '))
a4 = str(input('qual o do quarto? '))

lista = [a1, a2, a3, a4]

random = random.choice(lista)

print(f'o aluno escolhido pra apagar o quadro foi {random}')

