frase = input(('diga seu nome completo pra saber se tem "Silva no nome": '))
minuscuro = frase.lower()
sem_espaços = minuscuro.split()

print('silva' in (sem_espaços))
