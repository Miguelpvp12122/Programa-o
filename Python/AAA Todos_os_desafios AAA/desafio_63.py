print('=='*15)
print('termo de Fibonacci')
print('=='*15)

n = int(input('diga quantos termos de Fibonacci você que: '))
tot = 0
f1 = 0
f2 = 1

print(f'{f1} > {f2} > ', end='')

while tot <= n:
    f3 = f1 + f2
    print(f' {f3} ')
    f1 = f2
    f2 = f3
    tot += 1
