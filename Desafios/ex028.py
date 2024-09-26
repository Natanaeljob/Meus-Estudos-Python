import random
from time import sleep
#Jogo de adivinhar

num = random.randint(1, 5)

print("\033[35m✓-"*20,"\033[m")
sleep(1)
print( "\033[34m Consegue adivinhar que número escolhi?\033[m" )
sleep(4)
print("\n \033[31mAposto que vai errar!!!\033[m")
sleep(1)
print( "\033[35m✓-"*20,"\033[m")
sleep(1)
ne = int( input( " \n Digite um número de 1 a 5 " ) )
sleep(1)
print( "\n \033[35m PENSANDO... \033[m" )
sleep(3)
if ne == num:
  print( "\n\033[32m Muito bem, você me venceu!\033[m" )
else:
  print( " \n \033[31mNão foi dessa vez, pensei no número {}\033[m,\n \033[32mtente outra vez!\033[m".format( num ) )