anos = int(input('qual seu ano de nacimento? '))
anos -= 2024

if anos >-9:
    print('você é um MIRIN.')
elif anos >-14:
    print('você é um NOVATO.')
elif anos >-19:
    print('você é um JUNIOR.')
elif anos >-20:
    print('você é um SÉNIOR.')
else:
    print('você é um MASTER.')

print({anos})