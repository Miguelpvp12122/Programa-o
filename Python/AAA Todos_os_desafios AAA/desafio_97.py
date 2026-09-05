def linhas(var):
    tam = len(var) + 4

    print('~' * tam)
    print(f'  {var}')
    print('~' * tam)


escreva = str(input('digite uma frase sem espaços no começo e no final: ')).capitalize()

linhas(escreva)
