print("Números impares e multiplos de 3:")
print("")
soma = 0
cont = 0
for c in range(3,501,6):
    if c % 3 == 0:
        cont += + 1
        soma = c + soma
print("A soma de todos {} valores. \nCorresponde a {}".format(cont, soma))
