from random import randint
from time import sleep

jogos = []
passa = []
condição = int( input( 'Quantos Sorteios? ') )

for c in range(0,condição):

    while True:
        x = randint(1,60)
        if x not in passa:
            passa.append(x)
        if len(passa) >= 6:
            passa.sort()
            jogos.append(passa[:])
            passa.clear()
            break
    
    sleep(2)
    print('')
    print(f'{c+1}° Jogo: {jogos[c]}')
