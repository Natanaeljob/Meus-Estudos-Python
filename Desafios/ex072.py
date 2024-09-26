dc = " "
c = op = 0
lista = ( "", "Bola de Futebol", "Bola de basquete", "Bola de Voley", "Bola de Tênnis", "Bola de golf", "Bola de Hand ball", "Bola de gude", "Bola de praia", "Bola de ping-pong", "Apito",
"Cone", "Corda", "Bambole", "Colete", "Chuteira", "Cesto", "Rede", "Garrafa de água", "Toalha", "Fita" )
lista1 = []
for item in range(1,len(lista)):
    print('{:2}: {}'.format(item, lista[item]))

while True:
    print("")
    while True:
        op = int( input( "Digite o número do seu desejo: ") )
        if 0 < op <= 20:
            break
        print("Revise a escolha.", end = " ")
    while dc not in "SN":
        print("")
        dc = str( input( "Mais alguma coisa?" ) )[0].strip().upper()
    lista1.insert(c, lista[op])
    if dc == "N":
        break
    else: dc = " "
    c += 1
    
print("")
print(f"Itens Escolhidos\n{lista1}")