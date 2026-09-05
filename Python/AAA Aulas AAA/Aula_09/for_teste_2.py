import random

orc = int(10)

hp = int(10)

dado = random.randint(1, 12)
dadoo = random.randint(1, 12)

for batalha in range(0, 2):
    bater = input('aperte ENTER pra atacar: ')
    if bater == '':
        orc -= dado
        print(f'seu ataque voi {dado}')
        print(f'vida do orc está {orc} ')
