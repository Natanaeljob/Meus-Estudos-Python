from datetime import date

anoa = date.today().year

anon = int(input(" Digite o ano em que nasceu: " ) )

idade = anoa - anon

print( " Você tem {} anos ".format(idade) )


if anon > anoa:
    print(" Esta pessoa não nasceu ainda rs\n Está tentando me enganar?")

elif idade >= 40:
    print( " Esta velhinho para isso. " )

elif idade < 18:
    p = 18 - idade
    print( " \033[32mAinda é jovem para isso!\033[m")
    
    print( " Ainda faltam {} anos para você se alistar. ".format( p ) )

elif idade == 18:
    print( " Está na hora de se alistar!!! ")

else:
    print( " \033[31m!!!Atenção!!!\033[m " )
    p = idade - 18 
    print( " Já se passaram {} anos que deveria ter feito. ".format( p ) )

if idade < 18:
    print( " Deve se alistar em {}".format( anoa - idade + 18) )

elif idade > 18:
    print( " Deveria ter se alistado em {}".format(anoa - idade + 18))



print( "~~" * 10 )
print( " Tenha um bom dia! " )
print( "~~" * 10 )