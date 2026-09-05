def notas(*dados, sit=False):
    '''
    dados -> todas as notas

    * sit == False
    nada acontecera

    * sit == True
    mostra a situação da media da pessoa
    '''

    num = 0
    for p in dados:
        num += p
    media = num / len(dados)

    print(f'temos {len(dados)} notas, a maior nota foi {max(dados)} e a menor é {min(dados)}, a media das notas é {media}', end='')

    if sit == False:
        print()
    
    elif sit == True:
        if media >= 8:
            print(', sit = BOA')
        elif media < 8 and media > 5:
            print(', sit = Razoravel')
        elif media < 5:
            print(', sit = Ruim')


notas(10, 7, sit=True)
help(notas)
