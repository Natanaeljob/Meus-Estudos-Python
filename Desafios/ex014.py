#Conversor de temperatura
tc = int( input( " Qual a temperatura em °C? " ) )
tf = ( tc*9/5 ) + 32

print("Temperatura correspondiente a {}{}{} F.".format("\033[33m",round(tf),"\033[m" ) )