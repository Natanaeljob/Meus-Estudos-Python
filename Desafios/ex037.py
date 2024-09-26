n = int( input ( " Digite um número: " ) )
print("""
Qual conversão deseja?

1 = Binário
2 = Octal
3 = Hexadecimal

""")

e = int(input( "Escolha: "))

if e == 1:
    nc = bin(n)
    print(nc)
elif e == 2:
    nc = oct(n)
    print (nc)
else:
    nc = hex(n)
    print(nc)