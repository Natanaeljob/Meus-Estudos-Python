from time import sleep
from random import randint

numeros = list()

def sorteio():
    print(f'Números Sorteados: ')
    for re in range(0,5):
        x = randint(1,10)
        print(x, end = ' ', flush = True)
        sleep(0.5)
        numeros.append(x)
    print('Fim!!')
    
def somapar(x):
    s = 0
    for re in numeros:
        if re % 2 == 0:
            s += re
    print(s)


sorteio()

print(f' A soma dos números pares é {numeros} é: ', end = '')

somapar(numeros)

