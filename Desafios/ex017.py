#Calcular hipotenusa
#cateto oposto, cateto adjacente
co = float( input( "Digite o cateto oposto: " ) )
ca = float( input( " Digite o cateto adjacente " ) )

hip =  (co ** 2 + ca ** 2) ** (1/2) 

print( """
O cateto oposto é {}
O cateto adjacente é {}
A hipotenusa é {:.2f}
""".format( co, ca, hip ) )