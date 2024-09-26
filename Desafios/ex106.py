def ajuda(x):
    print(f'\033[44m Acessando manual do comando "{x}"')
    print(f'\033[7m{help(x)}')
    
while True:   
    print('\033[42m~'*32)
    print(f'{"SISTEMA DE AJUDA PyHELP":32}')
    print(f'{"~"*32}\033[m')
    
    ajuda(str(input('Função ou Biblioteca: ')))
    if ajuda == 'fim':
        break