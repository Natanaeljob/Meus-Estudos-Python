print( " Digite suas notas: " )

nota1 = float( input( "\n Primeira nota " ) )
nota2 = float( input( " Segunda nota " ) )

media = (nota1 + nota2) / 2

if media < 5 :
    print( "\n\033[31m Infelizmente reprovado " )
elif media >= 5 and media < 7:
    print( "\n\033[35m Está de recuperação!\n Ainda pode ser aprovado " )
else:
    print( "\n\033[32m PARABÉNS ESTÁ APROVADO!!!")

print( "\n Sua média foi de {:.2f} pontos ".format( media ) )