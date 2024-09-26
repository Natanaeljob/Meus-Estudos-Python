#Calculo de vendas

print("¿?"*7 + " HUNTER " + "¿?"*7)

print( "Referente a compra. \n\n Qual o valor do produto?" )

produto = float( input( " \n Valor das compras: R$ " ) )

print("\033[33m" + "Opções de pagamento:" + "\033[m")
print("""
A vista/ cheque     : 1
A vista no cartão   : 2
Parcelado no cartão : 3
""")

fp = int( input( "Qual a forma de pagamento? " ) )

c2 = "\033[36m"
c1 = "\033[31m"
c = "\033[32m"
f = "\033[m"

if fp == 1:
    print(" Cheque   : 1 \n Dinheiro : 2")
    escolha = int( input(" Opção 1 ou 2? ") )
    if escolha == 1:
        d = "Em cheque"
    else:
        d = "Em dinheiro"
    
    p = 10 / 100
    j = produto * p
    o = "Desconto: 10% / {}R$ {:.2f}".format( c, j )
    valor = produto - ( produto * p )

elif fp == 2:
    p = 5 / 100
    j = produto * p
    d = "A vista no cartão"
    o = "Desconto: 5% / {}R$ {:.2f}". format( c, j )
    valor = produto - ( produto * p )
    
elif fp == 3:
    parcelas = int( input( "Quantas parcelas? " ) )
    
    if parcelas > 2:
        p = 20 / 100
        valor = produto + ( produto * p )
        j = produto * p
        vp = valor / parcelas
        d = "Em {} vezes no cartão".format( parcelas )
        o = """Valor p/ parcela: R$: {}{:.2f}{}
    Juros: 20% / {}R$ {:.2f}{}""".format( c, vp, f, c1, j, f )

    else:
        valor = produto
        vp = valor / parcelas
        d = "Em {} vezes no cartão".format( parcelas )
        o = """Valor p/ parcela: R$: {}{:.2f}{}
    Sem juros""".format(c, vp, f)

if fp < 1 or fp > 3:
    print( "{}Opção inválida!".format(c1) )
    print( "Reinicie o programa e tente novamente!" )

else:
    print( """
    Compra {}!!!APROVADA!!!{} 
    Modo: {}. 
    Valor: {}R$ {:.2f}{}
    {}""".format( c2, f, d, c, valor, f , o ) )