#frase = str(input('digite um nome de uma cidade pra saber se nela tem o nome "Santo": '))
#minuscura = frase.lower()

#print('santo' in (minuscura))


cid = str(input('em que cidade voce nasceu? '))
minuscuro = cid.lower()
sem_espaços = minuscuro.split()
print(sem_espaços[:5] == ['santo'])
