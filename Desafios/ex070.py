nome = op = nomep =""
soma = preco = qtdd = mv = 0

print(f" {'Americanas':~^36} ")

while True:
    print("~"*36)
    nome = str( input( "Produto: " ) )
    preco = float( input( "Valor: R$ " ) )
    print("~"*36)
    
    if preco > 1000:
        qtdd += 1
    elif mv == 0:
        mv = preco
        nomep = nome
    elif mv > preco:
        mv = preco
        nomep = nome

    op = str( input( "Mais? [S/N]: " ) ).strip().upper()[:1]
    soma += preco

    while op != "S" and op != "N":
        op = str( input( "Mais? [S/N]: " ) ).strip().upper()[:1]
    if op == "N":
        break

print(f"{'Comprovante':~^36}")
print("Total gasto: R$ {}{:.2f}{} reais.".format("\033[32m",soma,"\033[m"))
print(f"{qtdd} produtos custam mais de R$ 1000.00 reais.")
print("Produto mais em conta {}{}{} que custa {}R$ {:.2f}{}.".format("\033[34m",nomep,"\033[m","\033[32m",mv,"\033[m"))
print("=-"*18)
