ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resposta = str(input('quer continuar? [S/N]: '))

    if resposta in 'Nn':
        break

print('=-'*30)
print(f'{"Nu.":<4}{'Nome':<10}{'Media':>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

while True:
    opc = int(input('quer ver a nota de qual aluno? [999 interrompe] '))

    if opc == 999:
        print('programa finalizado')
        break

    if opc <= len(ficha) - 1:
        print(f'nota de {ficha[opc][0]} é {ficha[opc][1]}')
