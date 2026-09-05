# DESAFIO QUE NÃO PEGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA







jogador = dict()
partidas = []
time = list()

while True:
    jogador.clear

    jogador['nome'] = str(input('qual o seu nome? '))
    tot = int(input(f'{jogador['nome']} você fez quantas partidadas? '))

    for p in range(0, tot):
        partidas.append(int(input(f'quantos gols você fez na partidada {p+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy)

    while True:
        continuar = str(input('quer continuar? [S/N]: ')).upper() [0]
        if continuar in 'NS':
            break
        print('ERRO digite entre S/N.')
    
    if continuar == 'N':
        break

for i, v in enumerate(time):
    print(f'{i} ', end='')
#:
#        print(f'{str(d)}', end='')
#    print()



print(time)