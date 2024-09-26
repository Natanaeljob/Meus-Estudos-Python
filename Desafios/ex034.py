s = float( input( "\033[33m" + "Digite seu salário " + "\033[m" ) )

a1 = 0.15
a2 = 0.10

ns = ( s * a2 ) + s
a = "10%"

if s <= 1250:
    ns = ( s * a1 ) + s
    a = "15%"

print("\033[32m" + " Seu salário recebeu {} de aumemto.\n Sendo assim de R$ {:.2f} reais para \n R$ {:.2f} reais.".format( a, s, ns ) )