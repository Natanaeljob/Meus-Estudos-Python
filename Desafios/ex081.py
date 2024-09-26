c = 1
x = -1
lista = []
while True:
    lista.append(valor = int( input(f'{c}° número: ')))
    c += 1
    op = ' '
    while op not in 'sn':
        op = str( input('Continuar? '))[0].strip().lower()
    if op == 'n':
        break
lista.sort(reverse = True)
if 5 in lista:
    x = lista.index(5)

print('')
print(f'{len(lista)} números digitados.')
print(f'O número 5 está na casa {x+1}.'if x != -1 else'O número 5 não foi digitado.' )
print('Lista decrescente: ',lista)