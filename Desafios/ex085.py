grupo = [[],[]]

for op in range(0,7):
    x = int( input( f'Digite o {op+1}° número: '))
    print('')
    if x % 2 == 0:
        grupo[0].append(x)
    else:
        grupo[1].append(x)
grupo[0].sort()
grupo[1].sort()

print(f'Números pares: {grupo[0]}')
print('')
print(f'Números ímpares: {grupo[1]}')