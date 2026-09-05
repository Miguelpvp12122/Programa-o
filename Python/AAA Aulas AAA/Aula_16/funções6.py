def soma(a = 0):
    global b
    # A variavel a é local se for modificada em dentro da função não mudara
    # A variavel b se torna global no momento que apricar o comando global no começo da função
    # Se a variavel b for modificada será modificada pra sempre
    a += 10
    b += 10

    print(f'a soma de a + 10 é iqual a {a}')
    print(f'a soma de b + 10 é iqual a {b}')


a = 0
b = 0

print(a)
print(b)

soma(a)

print(a)
print(b)
