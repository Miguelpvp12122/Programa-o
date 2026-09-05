pessoa = dict()
todos = list()

tot = soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    tot += 1
    todos.append(pessoa.copy())

    while True:
        continuar = str(input('quer continuar? [S/N]: ')).upper() [0]
        if continuar in 'NS':
            break
        print('ERRO')
    
    if continuar == 'N':
        media = soma / tot
        break

print('=='* 30)
print(f'temos {tot} pessoas cadrastadas') # pode ser também {len(todos)}
print(f'a media de idade é {media}')
print(f'nesse grupo existe tais mulheres: ', end='')
for a in todos:
    if a['sexo'] == 'F':
        print(f'{a['nome']}', end=' ')
print()
print('lista de pessoas acima da media de idade: ')
for p in todos:
    if p['idade'] > media:
        for k, v in p.items() :
            print(f'{k} = {v}', end=' ')
