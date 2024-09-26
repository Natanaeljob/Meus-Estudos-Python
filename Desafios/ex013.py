#Para salários maiores de 1500 aplicar aumento de 10%
#Para salários menores aplicar 15%

sal = float( input( "Qual o valor do salário? ") )
a1 = 15/100

aumento = sal + ( sal * a1 )
print( " Seu salário de R$ {:.2f} aumentou para {}R$ {:.2f}{} com 15% de aumento.".format(sal,"\033[32m",aumento,"\033[m" ) )