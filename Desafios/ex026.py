#Testando string

linha = str( input( "Digite algo: " ) ).strip().lower()

op1 = linha.count("a")#Contar caracteres
op2 = linha.find("a")+1
op3 = linha.rfind("a")+1

print("""
\033[32mA letra "A" aparece: {} vezes\033[m
A primeira na casa: {}
A segunda na casa: {}
""".format(op1, op2, op3) )