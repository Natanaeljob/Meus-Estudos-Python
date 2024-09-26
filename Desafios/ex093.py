print(' Aproveitamento de jogador')
print('')

c1 = '\033[32m'
c2 = '\033[33m'
c3 = '\033[34m'
f = '\033[m'

jogador = dict()
gol = list()
tot = 0

print(c1,'_'*30,f)
print('')

jogador['nome'] = str( input( ' Nome: ')).strip().upper()

print('')

Partidas = int( input( f' Número de partidas do jogador {jogador["nome"]}: '))

print(c1,'_'*30,f)
print('')

for re in range(0, Partidas):
    gol.append(int( input( f' Quantos gols na {re+1}ª partida? ')))
    print(c2,"_"*30,f)
    print('')

jogador['gols'] = gol[:]
jogador['total'] = sum(gol)

print(c1,'_'*30,f)
print('')
print(jogador)
print(c1,'_'*30,f)
print('')

for v, k in jogador.items():       
    print(f' O campo {v} tem o valor: {k}')

print(c3,'_'*30,f)
print('')

print(f'O jogador {jogador["nome"]} jogou {Partidas} jogos')

print(c3,'_'*30,f)
print('')

for i, g in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {g} gols')
print('')
print(f' Foi um total de {jogador["total"]} gols.')
print(c3,'_'*30,f)
