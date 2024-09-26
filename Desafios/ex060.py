print("Fatorial")
"""print("")

n = int( input( "Digite um número: " ) )
c = n
op = 1

print( "{}!".format(n), end = "")

while n != 0:
    
    print(c , end = "")   
    print("x" if c != 1 else "= ", end ="" )
    op *= c
    c -= 1
    
print(op)"""

numero = int(input("n ") )
aux = 1
print( "{}!".format(numero), end = "" )

for re in range(numero,0,-1):
    print(re, end = "")
    print( "x" if re > 1 else "= ", end = "" )
    aux *= numero
    numero -= 1
print(aux)