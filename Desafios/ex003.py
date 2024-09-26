n1=float(input("Digite o primeiro número. "))
n2=float(input("Digite o segundo número. "))

sun=n1+n2
sub=n1-n2
mult1=n1*n2
div1=n1/n2

div=round(div1,3)
mult=round(mult1,3)
#print("div.1 {} \n div.2 {}".format(div1,div2))

print("A soma entre {} e {} é \n igual a {}".format(n1,n2,sun))
print("A subtraçao entre {} e {} é \n igual a {}".format(n1,n2,sub))
print("A multiplicação entre {} e {} é \n igual a {}".format(n1,n2,mult))
print("A divisão entre {} e {} é \n igual a {}".format(n1,n2,div))
