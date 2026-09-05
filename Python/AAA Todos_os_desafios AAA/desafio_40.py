media1 = float(input('qual a primeira media do aluno? '))
media2 = float(input('qual a segunda? '))
media3 = float(input('qual a terceira? '))
media4 = float(input('e a quarta? '))
media5 = media1 + media2
media6 = media3 + media4
media7 = media6 + media5
total = media7/4

if total <5.0:
    print('reprovado :(')
elif total <6.9:
    print('recupelação')
else:
    print('aprovado :D')