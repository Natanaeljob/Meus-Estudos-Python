from datetime import date

ano = int( input( " Digite o ano em que nasceu: " ) )
idade = date.today().year - ano

f = "\033[m"

if idade <=9:
    p = "MIRIM"
    c = "\033[36m"
elif idade <=14:
    p = "INFANTIL"
    c = "\033[32m"
elif idade <=19:
    p = "JUNIOR"
    c = "\033[33m"
elif idade <=20:
    p = "SÉNIOR"
    c = "\033[35m"
else:
    p = "MASTER"
    c = "\033[31m"

if idade <= 0:
    print( "\033[31m Engraçadinho")
else:
    print( """ Você tem {} anos.\n Bem vindo(a) a equipe {}{}{}.
    """. format( idade, c, p, f ) )