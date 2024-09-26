geral = []

while True:
    nome = str( input( ' Aluno: '))
    nota1 = float( input( ' 1ª Nota: '))
    nota2 = float( input( ' 2ª Nota: '))
    media = (nota1 + nota2) / 2
    geral.append([nome,[nota1,nota2] ,media])
    
    op = ' '
    while op not in 'SN':
        op = str( input( 'Continuar? [S/N] '))[0].strip().upper()
    if op == 'N':
        break
dp = 0

print(f'{"No.":<4}{"nome":<10}{"Méd":>4}')
for i, re in enumerate(geral):
    print(f'{i+1:<4}{re[0]:<10}{re[2]:>4.2f}')
    
while dp != 999:
    dp = int( input( 'Mostrar qual Aluno ? '))
    if dp == 999:
        break
    print(f' O aluno {geral[dp-1][0]} teve as notas {geral[dp-1][1]}.')
