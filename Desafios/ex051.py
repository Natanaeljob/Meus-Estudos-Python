print("Progressão (PA)")
print("\n")

q = int( input( 'Quantidade: ' ) )
c = int( input( "Condição: " ) )

for re in range(c,q,c):
    print(re, end = "")
    if re < q:
        print(",", end = " ")
    else:
        print(".", end = "")