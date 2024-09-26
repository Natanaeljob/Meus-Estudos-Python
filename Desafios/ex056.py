idd = 0
ano = 0
nomemm = ""
anot = 0
qttf = 0
qttm = 0

for re in range (1,5):
    
    print("{}[{}]{}".format("~" * 9, re, "~" * 9 ) )
    nome = str( input( "Nome: " ) ).strip()
    print("")
    idade = int( input( "Sua idade: " ) )
    print("")
    sexo = str( input ( "Sexo [M/F]: " ) ).upper().strip()
    print("")
    idd += idade
    print("~" * 21)
    
    if sexo == "M":
        qttm += +1
        if ano == 0:
            ano = idade
        if idade >= ano :
            ano = idade
            nomemm = nome
            
    elif sexo == "F":
        qttf += +1
        if idade < 21:
            anot = anot + 1

media = int(idd/4)

print( " Pessoas entrevistadas: \n {} mulheres e {} homens.".format( qttf, qttm ) )
print("")
print( " Média de idade entre eles {} anos.".format( media ) )            
print("")
print( " Homem mais velho: {}, {} anos.".format( nomemm, ano ) )
print("")
print( " Mulheres menores de 21: {} mulheres.".format( anot ) )