#Desconto
produto = float( input( "Quanto custa o produto? " ) )
pc = 5/100
pd = produto - ( produto * pc )

print( "O produto de {}R$ {}{}, recebeu 5% de desconto, ficando por {}R$ {}{}.".format("\033[31m",produto,"\033[m","\033[32m",pd,"\033[m"))
