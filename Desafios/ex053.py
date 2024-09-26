print("Frase polindroma")
f = str( input( " Digite aqui: " ) ).lower().split()
f = "".join(f)
if f[::-1] == f:
    print("É polindroma")
else:
    print("Não é polindroma")