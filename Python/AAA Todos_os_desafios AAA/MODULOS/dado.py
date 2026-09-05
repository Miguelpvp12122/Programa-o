def nobreak(num):
    varido = False

    while not varido:
        msg = str(input(num)).replace(',', '.').strip
        if msg.isalpha() or msg == '':
            print(f'\033[31m ERRO {msg} não é um preço \033[m')
        
        else:
            varido = True
            return float(msg)
        