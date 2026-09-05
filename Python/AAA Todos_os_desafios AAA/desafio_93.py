jogador = dict()
partidas = []

jogador['nome'] = str(input('qual o seu nome? '))
tot = int(input(f'{jogador['nome']} você fez quantas partidadas? '))

for p in range(0, tot):
    partidas.append(int(input(f'quantos gols você fez na partidada {p+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=='* 30)
print(f'o nome do jogador é: {jogador['nome']}.')
print(f'em cada partida ele fem {partidas} gols')
print(f'e juntando tudo da {jogador['total']}')
print('=='* 30)
print(f'o jogador {jogador['nome']} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'na partida {i+1} fez {v} gols')
