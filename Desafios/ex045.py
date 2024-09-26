#jokenpo
import random
import time

lista = ("pedra", "papel", "tesoura")

pc = random.choice(lista)

print("Vamos jogar Pedra, papel, tesoura!!?")
time.sleep(2)
print("Aposto que vou vencer")
time.sleep(2)
player = str( input( " Escolha um !! ") )

if player == "pedra" or player == "papel" or player == "tesoura":
  time.sleep(2)
  print("JO")
  time.sleep(2)
  print("KEN")
  time.sleep(2)
  print("PO")
  time.sleep(2)

  print("//" * 20)
  
  if player == pc:
  
    print( " Empate, mas que sorte você tem :3 " )

  elif pc == "pedra" and player == "tesoura":
    print( " !!Sou muito bom!! " )

  elif pc == "papel" and player == "pedra":
    print( " !! Sem chance pra você !! ")

  elif pc == "tesoura" and player == "papel":
    print( " !! Você é um perdedor !! " )

  else:
    print( "\033[32m" + " !! Você finalmente venceu!! " + "\033[m" )

  print("//" * 20)

  print("Escolhi {} e você escolheu {}".format( pc, player ) )
else:
  print( " !! Opção inválida !! " )