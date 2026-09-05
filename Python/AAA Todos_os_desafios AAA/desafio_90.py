dict = dict()

dict['nome'] = str(input('digite o nome do aluno: '))
dict['media'] = float(input(f'qual a media de {dict['nome']}: '))
print('\n')

print(f'o nome é: {dict['nome']}, e sua a media é: {dict['media']}')

if dict['media'] >= 7:
    print(f'{dict['nome']} passou de ano')
elif dict['media'] < 7:
    print(f'{dict['media']} pelo visto não passara de ano')
    