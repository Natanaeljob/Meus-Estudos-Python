print("Soma de números pares")

soma = 0

for re in range(0,6):
    n = int( input( "Digite o número? " ) )
    if n % 2 == 0:
        soma += n

print(" A soma dos números pares corresponde a: {}".format( soma ) )