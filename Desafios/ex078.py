n = []
maior = menor = 0

for re in range(0,5):
    n.append( int( input( f'{re+1}° número: ' ) ) )
    
    if maior == 0 == menor:
        maior = menor = n[re]

    if maior < n[re]:
        maior = n[re]

    if menor > n[re]:
        menor = n[re]

print('')
print(n ,'\n')

print(f'O maior número é {maior} posicionado na casa: ')
for lugar, valor in enumerate(n):
    if valor == maior:
        print(f'{lugar}...', end = '')
print('')
print(f'O menor número é {menor} posicionado na casa:')
for lugar, valor in enumerate(n):
    if valor == menor:
        print(f'{lugar}...', end = '')