# 50 20 10 1
print("{:_^36}".format( 'Banco CIV' ) )
cen = vin = dez = uni = 0
cont = saq = valor = 0
v = "\033[32m"
c = "\033[36m"
f = "\033[m"
while True:
    
    valor = float( input( 'Quanto quer sacar? R$ {}'.format(v) ) )
    print(f)
    
    if saq == 0:
        saq = valor

    while saq >= 50:
        cen += 1
        saq -= 50
    while saq >= 20:
        vin += 1
        saq -= 20
    while saq >= 10:
        dez += 1
        saq -= 10
    while saq >= 1:
        uni += 1
        saq -= 1
    if saq < 1:
        break
    
print(f"{'Extrato':~^36}")

print("Valor sacado: {}R$ {:.2f}{} reais".format( v, int(valor), f ) )

if cen > 0:
    print("Total de cédulas de 50 reais: {}{}{}".format(c, cen, f) )
if vin > 0:
    print("Total de cédulas de 20 reais: {}{}{}".format(c, vin, f) )
if dez > 0:
    print("Total de cédulas de 10 reais: {}{}{}".format(c, dez, f) )
if uni > 0:
    print("Total de cédulas de 1 real: {}{}{}".format(c, uni, f) )

print("~"*36)