somadeidade = 0
mediadeidade = 0
idadeM = 0
idadem = 0
for A in range(1, 5):
    print(f'======={A}ª=======')
    nome = input('qual o nome: ')
    idade = int(input('qual a idade: '))
    sexo = input('qual o sexo (M/F): ')
    if sexo == 'M':
        if A == 1:
            A = idadeM
            A = idadem
        else:
            if A > idadeM:
                maior = A
            elif A < idadem:
                menor = A
    somadeidade += idade
media = somadeidade / 4
print(f'A media do grupo é {media}.')
print(f'A pessoa mais velha é {maior}.')
