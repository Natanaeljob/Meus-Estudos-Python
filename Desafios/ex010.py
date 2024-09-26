#Conversão de moeda
#Dollar: 3.27
real=float(input("Quanto você tem na carteira? R$"))
dollar=3.27
conversao=real/dollar

print("Com {}R${}{} você pode comprar: \n{}${:.2f}{} dólares.".format("\033[4;32m",real,"\033[m", "\033[4;32m",conversao,"\033[m" ) )