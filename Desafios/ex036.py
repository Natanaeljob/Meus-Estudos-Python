casa = float( input( "Quanto custa a casa? R$ " ) )
salario = float( input( "Qual seu salário? R$ " ) )
tempo = int( input( "Quantos anos vai pagar? R$ " ) )

parcela = casa / (tempo * 12)
cento = salario * 0.30

print( "\n Uma casa de R$ {:.2f} reais, tem uma parcela de R$ {:.2f} reais por mês em {} anos.".format( casa, parcela, tempo) )

if parcela <= cento:
    print( "\033[32m" + " EMPRESTIMO APROVADO!!!" + "\033[m" )
else:
    print( "\033[31m" + " EMPRESTIMO NEGADO!!!" + "\033[m" )