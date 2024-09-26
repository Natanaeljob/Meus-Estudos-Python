print("Números pares de 1 a 50:")

for c in range(2,51,2):
    print( c, end = "" )
    if c < 50:
        print( ", ", end = "" )
    else:
        print(".")