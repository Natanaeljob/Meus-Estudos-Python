m1 = int( input( "medida 1: " ) )
m2 = int( input( "medida 2: " ) )
m3 = int( input( "medida 3: " ) )

if m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
    print( "\033[32m" + " Essas medidas podem se tornar\n Um triângulo!!!" )
else:
    print( "\033[31m" + " Essas medidas não formam um triângulo")