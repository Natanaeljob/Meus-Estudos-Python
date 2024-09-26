print("Tabuada")
print("\n")

tabu = int( input( "Qual deseja? " ) )
print("\n")

f = "\033[m"

for re in range(0,11):
    if re % 2 == 0:
        c = "\033[35m"
    else:
        c = "\033[36m"
    print("{}{}{}x{}{:2}{}={}{}{}".format( c, tabu, f, c, re, f, c, re * tabu, f ) )