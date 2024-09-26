sexo = ""

while sexo != "M" and sexo != "F":
    
    sexo = str( input("Digite seu sexo [M/F]: " ) ).strip().upper()[0]
    
    if "F" != sexo != "M":
        print("Falha, tente novamente! ")

    else:
        print("Obrigado por participar!!")