#Comparando valores

n1 = int( input( "Digite o primeiro valor: " ) )
n2 = int( input( "Digite o segundo valor: " ) )

f = "\033[m"
c2 = "\033[33m"

if n1 > n2:
    c = "\033[36m"
    r = "é maior que"
elif n1 < n2:
    c = "\033[32m"
    r = "é menor que"
else:
    c = "\033[35m"
    r = "é igual ao"
print( " O número {}{}{} {} {}{}{}. ".format( c, n1, c2, r, c, n2, f ) )