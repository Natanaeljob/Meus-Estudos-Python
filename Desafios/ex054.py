from datetime import date
atual = date.today().year
op = 0

for re in range( 0 , 7 ):
    ano = int( input( "Ano de Nascimento {}: ".format(re+1) ) )
    cd = atual - ano
    if cd >= 21:
        op = op + 1
print("\n")
print( " {} datas de nascimento são maiores de idade.".format(op) )