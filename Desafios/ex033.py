n1 = int( input( "\033[33m" + "Digite o primeiro: " ) )
n2 = int( input( "\033[34m" + "Digite o segundo: " ) )
n3 = int( input( "\033[35m" + "Digite o terceiro: " ) )

numeros = ( n1, n2, n3 )
print("""
\033[32m{} é o maior.
\033[31m{} é o menor.
""".format( max(numeros), min(numeros) ) )
