#Escreva um programa que leia a velocidade 
#de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que
#ele foi multado. A multa vai custar
#R$7,00 por cada Km acima do limite.

velocidade = int( input( " Qual a velocidade? " ) )
vp = 80
vmulta = 7
if velocidade <= 80:
    c = "\033[32m"
else:
    c = "\033[31m"

print( "\n{} Velocidade de {} Km/h.\033[m".format( c, velocidade ) )

if velocidade <= 80:
    print("\033[36m\n Bom condutor, siga viagem!!!\033[m")
else:
    multa = (velocidade - vp) * vmulta
    print("\033[31m\n !!!! Infração !!!!\n Veículo multado em:\n R$ {:.2f} reais. \033[m".format(multa))
