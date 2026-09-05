from time import sleep

def ajuda(com):
    print(f'\033[35mavaliando a função {com}\033[m')
    sleep(1)
    print('\033[34m')
    help(com)
    print('\033[m')

def linha(linha):
    print('\033[31m')
    tam = int(len(linha)) + 4
    print('=' * (tam))
    print(f'  {linha}')
    print('=' * (tam))
    print('\033[m')


comando = ''
while True:
    linha('Funções de PYTHON')
    comando = str(input('Função ou biblioteca: '))

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

linha('Até logo')
