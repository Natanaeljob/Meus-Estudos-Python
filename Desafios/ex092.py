import datetime

car = ' '
anoa = datetime.date.today().year
dados = dict()

dados['nome'] = str(input('Nome: '))
dados['ano'] = int( input('Ano de nascimento: '))
dados['idade'] = anoa - dados['ano']
 
dados['CTPS'] = str( input(' Número da CTPS (digite 0 se não tem) : '))[0].strip().upper()

if dados['CTPS'] == 0 :
    dados['CTPS'] = 'Não possuí CTPS'
else:
    dados['Contratação'] = int( input( 'Ano de contratação: '))
    dados['salario'] = float( input('Salário: \033[32mR$'))
    print('\033[m\n')
    dados['Aposentadoria'] = (dados['Contratação'] - dados['ano']) + 35

for v, k in dados.items():
    print(f' {v} tem o valor {k}')
