#.strip remove espaços
n= str( input( " Digite seu nome completo " ) )

maiusculo = n.upper()
minusculo = n.lower()
qcaracteres= len(n) - n.count( " " ) 
separar = n.split()
qnome = len( separar[ 0 ] )

print("""
Seu nome Maiúsculo: {}
Seu nome Minúsculo: {}
Seu nome Possui {} letras.
Seu primeiro nome tem {} letras.
""".format( maiusculo, minusculo, qcaracteres, qnome ) )