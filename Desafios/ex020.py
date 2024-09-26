import random
a1 = str( input( "Nome de um aluno" ) )
a2 = str( input( "Nome de outro aluno" ) )
a3 = str( input( "Nome de mais um aluno" ) )
a4 = str( input( "Nome de outro aluno" ) )

lista = [a1, a2, a3, a4]

print( "A ordem de apresentação será" )
print(random.sample(lista, k=4) )