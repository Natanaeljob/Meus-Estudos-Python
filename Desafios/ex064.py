n = s = c = 0
print("Digite 999 para desligar")
while n != 999:
    n = int( input( "Número: " ) )
    if n != 999:
        s += n
        c += 1
    print("")
print ("Soma: ",s)
print("Números digitados: ",c)