lista = [[],[],[]]
par = tc = m2 = 0

for te in range(0,3):    
    for re in range(0,3):

        x = int(input( f'Digite um valor para: [{te}, {re}]'))
        lista[te].append(x)
        
        if x % 2 == 0:
            par += x
        
        if te == 1:
            if m2 == 0:
                m2 = x
            else:
                if m2 < x:
                    m2 = x
        
        if re == 2:
            tc += x

for c in range(0,3):
    for re in lista[c]:
        print(f'[{re:^7}]', end = ' ')
    print('')

print('')
print(f'Soma dos números pares: {par}')
print(f'Soma da terceira coluna: {tc}')
print(f'Maior número da linha 2 é: {m2}')
