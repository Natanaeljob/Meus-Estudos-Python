def ficha():

    nome = str( input( ' Nome do jogador: '))
    gols = str( input( ' Quantos gols? '))
    
    if nome == '':
        nome = 'Desconhecido'
    
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    
    return f'O jogador {nome} fez {gols} gols no campeonato.'


print(ficha())