lista = []
y = ' '
c = 1

print('\033[34m', '_'*36, '\033[m')
while True:
    
    x = int( input( f'{c}° Número:\033[36m ' ) )
    c += 1
    print('')
    if x not in lista:
        print('\033[32mAdicionado')
        lista.append( x )


    else:
        print('\033[31mRepitido. ', end = '')
    
    while y not in 'sn' :
        y = str( input( '\033[33m\nContinuar? [S/N] \033[m' ) )[0].lower().strip()
    print('\033[34m', '_'*36, '\033[m')
    if y == 'n':
        break
    y = ' '
    
lista.sort()

print(f'\033[35mLista ordenada:\033[m {lista}')
print('\033[34m', '_'*36, '\033[m')
