lista = []
op = 0
print(' Números crescentes:')
print('')

for re in range (0,int( input('Quantos números você quer? '))):
    
    print('{}{:_^36}{}'.format('\033[34m','_','\033[m'))
    x = int( input(f'{re+1}° número: '))
    print('')
    
    if re == 0 or x > lista[-1]:
        lista.append(x)
        print('Colocado na ultima posição.')

    else:
        for op in range(0,len(lista)):
            
            if x <= lista[op]:
                lista.insert(op,x)
                print(f'Colocado na posição: {op}')
                break


print('{}{:_^36}{}'.format('\033[32m','_','\033[m'))
print('')
print(f' \033[36mLista ordenada\033[m {lista}')
print('{}{:_^36}{}'.format('\033[32m','_','\033[m'))
