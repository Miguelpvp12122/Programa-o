def soma(* lis): # valores opcionais
    num = sum(lis)

    print(f'a soma entre ', end='')
    for a, b in enumerate(lis):
        print(f'{b} + ', end='')

    print(f'= {num}')

soma(10, 50, 60, 50)