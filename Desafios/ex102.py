from função import *

def fatorial(n, show = False):
    '''
    fatorial (n, show = False)
    --> Calcula o Fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (Opcional) Mostrar ou não mostrar calculo.
    :return: Valor fatorial de um número.
    '''
    if show == True:
        print(f'{n}!=', end = '')
    M = 1
    for re in range(n,0,-1):
        M *= re
        if show == True:
            print(f'{re}', end = '')
            if re > 1:
                print('x', end = '')
            else:
                print('= ', end = '')
            
    return M
ls('-')

print(fatorial(5,True))