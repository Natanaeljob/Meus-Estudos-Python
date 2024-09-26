#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = 0.15

dia = 60

qd = int( input( " Quantos dias ficou alugado? " ) ) 
qk = float( input( " Quantos Km rodados? " ) )

c1 = dia * qd

c2 = qk * km

cf = c1 + c2

print( " O valor a ser pago pelos {}{}{} dias e {}{}{} Km rodados é de {}R$ {:.2f}{}".format( "\033[35m", qd, "\033[m", "\033[33m", qk, "\033[m", "\033[32m", cf, "\033[m" ) )
