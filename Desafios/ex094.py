pessoas = list()
dados = dict()
idade = 0

print('\033[34m' , '_'*36, '\033[m',)

while True:

    dados.clear()
    dados['nome'] = str( input( 'Nome: ')).strip().upper()
    while True:
        dados['sexo'] = str( input( 'Sexo [M/F]: '))[0].strip().upper()
        if dados['sexo'] in 'MF':
            break
        print(f'"{dados["sexo"]}" não contém na resposta...', end = '')
    dados['idade'] = int( input( 'Idade: '))
    idade += dados['idade']
    print('\033[34m' , '_'*36, '\033[m',)

    pessoas.append(dados.copy())
    while True:
        x = str( input( ' Continuar? ')).upper().strip()
        if x in 'SN':
            break
        print(f'"{x}" não contém na resposta...', end = '')
    if x == 'N':
        print('\033[31m' , '_'*36, '\033[m',)
        break
    print('\033[32m' , '_'*36, '\033[m',)

print(f' O grupo tem {len(pessoas)} pessoas.\n')

md = idade / len(pessoas)
print(f' A média de idade do grupo é {int(md)} anos.\n')

print(' As mulheres cadastradas foram:\033[33m ', end = '')
for op in pessoas:
    if op['sexo'] == 'F':
        print(op['nome'], end = '. ')
print('\033[m\n')

print('Pessoas a cima da média:\n')
for op in pessoas:
    if op['idade'] >= md+5:
        for v, k in op.items():
            print(f' {v} = \033[31m{k}\033[m', end = ' '*3)
        print('')

print('\033[34m' , '_'*36, '\033[m',)
