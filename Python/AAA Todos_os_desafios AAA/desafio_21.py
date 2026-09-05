frase = input('digite seu nome completo: ')

upper = (frase.upper())

lower = (frase.lower())

dividido = frase.split()
junsao = ''.join(dividido)
contando = len(junsao)

primeiro_nome = dividido[0]
final = len(primeiro_nome)

print(f'seu nome completo em letra mais uscura é {upper} ele todo em minuscura é {lower} seu nome tem {contando} letras e so o primeiro nome tem {final}')
