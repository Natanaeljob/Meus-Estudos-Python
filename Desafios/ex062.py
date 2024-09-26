print( "PA")

n = int( input("Termo: "))
c = int( input( "condiçao: "))
op = 0
d = 10
p = ""

while op != d:
    
    op += 1
    n += c
    
    print(n , end = " ")
    
    if op == d:
        print("")
        p = int( input(" Gostaria de mais quantos termos? ") )
        d += p

print("Processo finalizado com {} termos.".format(op))
print(" Obrigado por usar. ")
