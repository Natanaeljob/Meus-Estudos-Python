idd = idf = sm = 0
op = ""

print("{}{:~^36}{}".format("\033[32m","Cadastro","\033[m"))
while True:
    
    idade = int( input("Idade: ") )
    
    while True:
        
        sexo = str( input( "[M/F]:" ) ).upper().strip()[:1]
        if "M" == sexo or sexo == "F":
            break

    if idd >= 18:
        idd += 1

    if sexo == "M":
        sm += 1

    if sexo == "F" and idade < 20:
        idf += 1

    op = str( input("Quer continuar?" ) ).upper().strip()
    
    while op != "S" and op != "N":
        op = str( input("Quer continuar?" ) ).upper().strip()
    
    if op == "N":
        break

    print("{}{:~^36}{}".format("\033[32m","","\033[m"))

print(f"{idd} pessoas tem +18 anos.")
print(f"{sm} homens cadastrados.")
print(f"{idf} mulheres tem menos de 20 anos.")