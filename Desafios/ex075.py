n = ( int( input(" n1: ")), int( input(" n2: ")), int( input(" n3: ")), int( input(" n4: ")))
n3 = 0
par = 0

if 3 in n:
    n3 = n.index(3)

print(f'Você digitou {n}')
print(f'Número 9 aparece {n.count(9)} vezes'if n.count(9) > 0 else 'Não tem número 9')
print(f'Número 3 está na casa {n3}'if n3 > 0 else 'Não existe número 3 na Tupla')
print(f'Os números pares são: ', end = "")
for re in n:
    if re % 2 == 0:
        print(re, end = " ")