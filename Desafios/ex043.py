print(" "+"/"*11)
print( " Calculo IMC " )
print(" "+"/"*11)

altura = float( input( "\n Qual a sua altura? " ) )
peso = float( input( " Qual é seu peso? " ) )

IMC = peso / ( altura * altura)
f = "\033[m"

if IMC < 18.5:
    r = "peso abaixo"
    c = "\033[36m"
    a = "Precisa de mais massa."
    
elif IMC >= 18.5 and IMC < 25:
    r = "peso ideal"
    c = "\033[32m"
    a = "Parabéns Continue assim!!!"
    
elif IMC >= 25 and IMC < 30:
    r = "sobre peso"
    c = "\033[33m"
    a = "Tome cuidado..."

elif IMC >= 30 and IMC < 40:
    r = "obesidade"
    c = "\033[35m"
    a = "Procure ajuda."
else:
    r = "obesidade mórbida"
    c = "\033[31m"
    a = "Precisa muito se cuidar!!!"
    
print("\n "+"//"*16)
print(" Você está com {}{}{} \n {}{}{}".format( c, r, f, c, a, f ) )
print(" "+"//"*16)
