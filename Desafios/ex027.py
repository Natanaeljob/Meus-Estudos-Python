nome = str( input( "Digite seu nome: " ) ).split()

print("Prazer em lhe conhecer!!!")
print("Seu primeiro nome é {}{}{}".format( "\033[35m", nome[0], "\033[m" ) )
print("Seu último nome é {}{}{}".format( "\033[36m", nome[-1], "\033[m" ) )