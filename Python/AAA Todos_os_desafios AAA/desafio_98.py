import time


def cont(A, B, C):
    if C < 0:
        C *= 1
    if C == 0:
        C = 1

    print('==' * 20)
    print(f'contagem de {A} até {B} de {C} e {C}')

    if A < B:
        cont = A
        while cont <= B:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += 1
        print('   ...Fim...')
    
    else:
        cont = A
        while cont >= B:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= C
        print('   ...Fim...')


cont(1, 10, 1)
cont(10, 0, 2)

print('==' * 20)
print('agora sua vez de fazer a contagem')
print('==' * 20)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

cont(inicio, fim, passo)
