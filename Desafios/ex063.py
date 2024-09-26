n = int( input( " Digite um número: " ) )
"""c = 0
s = 1
op = [0]

while (c+1) != n :
    
    s += op[(c - 1)]  
    c += 1
    op.insert(c,s)

forma = str(op)[1:-1]
forma.split()
"".join(forma)


print(" {} < FIM".format(forma.replace(","," < ") ) )"""

a = 0
b = 1
c = 0
d = 3

print(a,b, end = " ")

while d <= n :
    c = a + b
    print(c, end = " ")
    a = b
    b = c
    d += 1