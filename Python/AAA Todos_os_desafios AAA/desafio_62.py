num1 = int(input('digite o primeiro numero: '))
num2 = int(input('digite um numero pra ser o PA dele: '))
termo = num1
tot = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while mais <= total:
        print(f' {num1} ', end='>')
        termo += num2
        tot += 1
    print('pausa')
    mais = input('quer digitar mais? ')
        
print('\n')
print('===FIM===')

