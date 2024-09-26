ano = int( input( "Digite o ano: " ) )

r = "não é BISSEXTO"
c = "\033[31m"

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    r = "é BISSEXTO"
    c = "\033[32m"

print( "{} O ano {} {}.".format( c, ano, r ) )