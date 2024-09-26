from random import randint
from time import sleep
from operator import itemgetter

jogos = dict()
ordem = []
maior = op = 0

for jg in range(0,4):
    jogos[f'jogador{jg+1}'] = randint(1,6)

for v, k in jogos.items():
    sleep(1)
    print(f'O {v} tirou {k}')

ordem = sorted(jogos.items(), key = itemgetter(1), reverse = True)
print('')

for i, o in enumerate(ordem):
    sleep(1)
    print(f'{i+1}° Lugar: {o[0]} com número {o[1]}')