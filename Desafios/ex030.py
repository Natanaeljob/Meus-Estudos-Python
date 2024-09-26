numero = int( input( "Digite um número: " ) )

t = "IMPAR"
c = "\033[35m"
if numero % 2 == 0:
    t = "PAR"
    c = "\033[34m"
print("{} O número {}\n É {} ".format(c, numero, t ) )