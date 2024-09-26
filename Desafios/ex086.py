lista = [[],[],[]]

for te in range(0,3):    
    for re in range(0,3):
        lista[te].append(int(input( f'Digite um valor para: [{te}, {re}]')))

for c in range(0,3):
    for re in lista[c]:
        print(f'[{re:^7}]', end = ' ')
    print('')