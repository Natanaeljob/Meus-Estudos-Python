pre = ( "Lapis", .5, "Caneta", 2.5, "Borracha", .5, "Apontador", 2.5, "Tesoura", 2.5, "Estojo", 5, "Compasso", 2.5, "Regua", 4, "Lancheira", 7.50, "Caderno", 20, "Papel Chamex", 3.5, "Mochila", 40 )
print('{:_^36}'.format("Ofertas"))
print('{:<20}{:>14}'.format("Produto", "Preço"))
print("")
for mat in range(0, len(pre),2):
    print('{:.<28}{}{:.2f}'.format(pre[mat], "R$ ",pre[mat+1]))
print("_"*38)