palavras = ('python', 'sonic', 'miranha', 'hulk', 'chines', 'guanabara', 'miguel_siguma', 'edson_beta', 'americano', 'godot', 'gbryel=chines', 'oruan', 'mauro', 'nobruzera', 'lula', 'bogonario')

for p in palavras:
    print(f'\nna palavra {p} temos............ ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print( letra , end=' ')    