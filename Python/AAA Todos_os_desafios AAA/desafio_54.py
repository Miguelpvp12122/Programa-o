from datetime import date
atual = date.today().year
totM = 0
totN = 0
for datas in range(1, 3):
    data = int(input('qual a data da pessoa? '))
    idade = atual - data
    if idade >= 18:
        totM += 1
    else:
        totN += 1
print(f'{totM} são pessoas maior de idade.')
print(f'{totN} são pessoas menores de idade.')
