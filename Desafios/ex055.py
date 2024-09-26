print("Maior e menor peso")
min = 0
max = 0
for re in range(0,5):
    p = float( input( "Digite o {} peso: kg ".format( re + 1 ) ) )
    
    if min == 0 and max == 0:
        min = p
        max = p
    if p > max:
        max = p
    elif p < min:
        min = p

print("Menor peso: {:.2f} kg \nMaior peso: {:.2f} kg".format( min, max ) )