from time import sleep
soma = 0
mult = 0
maior = 0
nn = 0
sair = 0
print("Digite dois números:")

while sair != 1 :
    print("")
    print("//"*15)
    n1 = float( input( "1° número: " ) )
    print("")
    n2 = float( input( "2° número: " ) )
    print("//"*15)

    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos númeroa
    [5] Sair do programa
    """)
    
    opu = int( input( "O que deseja? " ) )
    print("")

    if 0 < opu < 6:

        if opu == 1:
            soma = n1 + n2

            if soma.is_integer() == True:
                soma = int(soma)
                
            else:
                soma = "{:.3f}".format(soma)

            print("Soma de {}+{} = {}".format(n1, n2, soma) )

        elif opu == 2:
            mult = n1 * n2
            
            if mult.is_integer() == True:
                mult = int(mult)

            else:
                mult = "{:.3f}".format(mult)
                
            print("Multiplicação {}x{}= {}".format(n1, n2, mult) )

        elif opu == 3:

            if n1.is_integer() == True and n2.is_integer() == True :
                n1 = int(n1)
                n2 = int(n2)

            print("{} maior que {}".format(n1,n2) if n1 > n2 else "{} é maior que {}".format(n2,n1) )

        elif opu == 4:
            print("Reiniando...")
            sleep(2)

        else:
            sair = 1
            print("Desligando...")
            sleep(2)
            
print("Obrigado por usar nosso Serviço!!!")