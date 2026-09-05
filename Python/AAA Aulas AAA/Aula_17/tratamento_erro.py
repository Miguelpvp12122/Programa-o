try:  # tente fazer tal coisa
    a = int(input('Digite o numero A: '))
    b = int(input('Digite o numero B: '))
    C = a / b

except ZeroDivisionError : # se caso isso aconteça digite tal coisa
    print('Um numero não pode ser dividido por 0!')
except ValueError :
    print('Digite um numero como um valor numerico')
except KeyboardInterrupt :
    print('o usurio parou 😔')

else:   # se der tudo certo faça tal coisa
    print(f'A divisão de A e B é {C}')

finally: # idependentemente se de certo ou errado faça tal coisa
    print(f'Obrigado! Volte sempre :D')
