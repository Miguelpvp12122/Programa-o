def jogador(nome, gols):
    if nome in '              ':
        nome = '<desconhecido>'
    if gols in '              ':
        gols = 0
    
    print(f'O jogador {nome} fez {gols} gol(s)')


nome = str(input('Qual o nome do jogador? '))
gols = str(input('Quantos gol(s) fez? '))

jogador(nome, gols)
