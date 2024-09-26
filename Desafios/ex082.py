c = 1
lista = []
par = []
impar = []
while True:
    
    lista.append( int( input(f'{c}° número: ')))

    c += 1
    op = ' '
    
    while op not in 'sn':
        op = str( input('Continuar? '))[0].strip().lower()
    
    if op == 'n':
        break

lista.sort()

for top in lista:
    if top % 2 == 0:
        par.append(top)
    else:
        impar.append(top)

print('')
print(f'Lista com todos os números:', end = ' ')

for re in range(0, len(lista)) :
    print(lista[re], end = '')
    
    if len(lista)-1 > re:
        print(', ', end = '')
    else:
        print('.')

print('')
print(f'Lista com pares {par}')
print('')
print(f'Lista com impares {impar}')