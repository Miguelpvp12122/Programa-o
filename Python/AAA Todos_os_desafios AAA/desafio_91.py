import random
import time
import operator

jogadores = dict()
rank = list()

tot = 0
tot2 = 0

jogadores['jogador_1'] = random.randint(1, 6)
jogadores['jogador_2'] = random.randint(1, 6)
jogadores['jogador_3'] = random.randint(1, 6)
jogadores['jogador_4'] = random.randint(1, 6)

for v in jogadores.keys():
    tot += 1
    print(f'jogador {tot} tirou {jogadores[v]}')
    time.sleep(0.7)

rank = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

print('=='* 30)
print('=== Rank de jogadores ===')

for i, v in enumerate(rank):
    print(f'    {i+1}ª {v[0]} com {v[1]}')
