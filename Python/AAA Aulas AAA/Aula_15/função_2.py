def lin():
    print('=='*25)

def núm(* num): # trasforma o parametro em uma tupla
    tam = len(num)
    lin()
    print(f'nos valores {num} eu encontrei {tam} numeros')
    lin()


núm(1, 10, 11)
