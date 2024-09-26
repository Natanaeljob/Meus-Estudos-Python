save = list()
ent = list()
maiorp = menorp = 0

while True:

    ent.append(str( input( 'Nome: \033[34m')))
    print('\033[m')
    ent.append(int( input( 'Peso: \033[33m')))
    print('\033[m')
    save.append(ent[:])

    if maiorp == 0 == menorp:
        maiorp = menorp = ent[1]
    else:
        if maiorp < ent[1]:
            maiorp = ent[1]
        if menorp > ent[1]:
            menorp = ent[1]

    ent.clear()
    
    op = ' '
    while op not in 'SN':
        op = str( input( 'Continuar ? [S/N] '))[0].strip().upper()
        print('')
    if op == 'N':
        break

print(f'Total de \033[32m{len(save)}\033[m pessoas participaram!!!')
print('')
print(f'Maior peso registrado \033[31m{maiorp}\033[mKg.')
print('')
print(f'Pertence à: ')
for p in save:
    if p[1] == maiorp:
        print(f'[ \033[35m{p[0]}\033[m ]', end = ' ')
print('\n')
print(f'Menor peso registrado \033[31m{menorp}\033[mKg.')
print('')
print(f'Pertence à: ')
for p in save:
    if p[1] == menorp:
        print(f'[ \033[35m{p[0]}\033[m ]', end = ' ')
