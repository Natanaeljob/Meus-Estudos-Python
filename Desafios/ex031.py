#Exercício Python 031: 
#Desenvolva um programa que pergunte 
#a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando
#R$0,50 por Km para viagens de até 200Km
#e R$0,45 parta viagens mais longas.

print("Qual a distância em km?")
percurso = float( input( "\n\033[36m Digite aqui! " ) )

p1 = 0.50 #até 200km
p2 = 0.45 #mais de 200km

valor = percurso * p2
t = "longa"

if percurso <= 200:
    valor = percurso * p1
    t = "curta"

print("\033[32m\n Sua viagem de {}\n Custará R$ {:.2f} reais. ".format( t, valor ) )
