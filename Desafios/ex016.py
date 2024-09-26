#cortando decimais
numero = float( input( "Digite um número quebrado " ) )

i = int( numero )
arr = round( numero)

print( """
Cortando fica {} 
Arredondando fica {}
""". format( i, arr ) )