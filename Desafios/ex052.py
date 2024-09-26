print( " Número primo? " )
n = int( input( " Digite seu número: " ) )

if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    if n == 2 or n == 3 or n == 5 or n == 7:
        r = " É PRIMO"
    else:
        r ="NÃO É PRIMO"
else:
    r = "É PRIMO"
print("O número dogitado {}. ".format(r))