salario = int(input('qual o valor do seu salario? '))

if salario >1250:
    desconto = salario*10/100
    total = desconto+salario
    print(f'seu salario ficou com {desconto} a mais do que o normal e o valor total {total}')
else:
    desconto2 = salario*15/100
    total2 = desconto2+salario
    print(f'seu salario ficou com {desconto2} a mais do que o normal e o valor total é {total2} ')