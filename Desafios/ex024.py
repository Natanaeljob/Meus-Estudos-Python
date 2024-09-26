#Detect se existe SANTO no primeiro nome
#duas formas

r = int( input( "Op 1 ou 2 ? " ) )
if r == 1:
    nome = str( input( "Digite o nome da cidade: " ) ).lower()
    nome = nome.split()
    nome =  nome[0].find("santo")
    print(nome)
else: 
    nome = str( input( "Digite o nome da cidade: " ) ).lower()
    nome = nome.split()
    nome = "santo" in nome[0]
    print( nome )