c = max = min = s = 0
op = ""

while op != "n":
    
    n = int( input("Número:"))
    
    s += n #Soma
    c += 1 #Contagem
    
    if max == 0:
        max = min = n
        
    if n > max:
        max = n
        
    if n < min:
        min = n
        
    op = str( input( " Continuar? " ) ).lower()

med = s / c

print("Muito bem..")
print("Soma dos números{}".format( s ) )
print("Media dos números: {:.3f}".format( med ) )
print("Maior número {}".format( max ) )
print("Menor número {}".format( min ) )