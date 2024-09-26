#Verificando se existe Silva no nome
r = int( input( "op 1 ou 2 ? " ) )
if r == 1:
    nome = str( input( "Digite seu nome completo: " )  ).strip()
    nome = nome.lower().find("silva")
    if nome != -1 :
        print("Contém Silva no seu nome.")
    else:
        print("Não contém Silva no seu nome.")
else:
    nome = str( input( "Digite seu nome completo: " ) )
    nome = "silva" in nome.lower()
    print()