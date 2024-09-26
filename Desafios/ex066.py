print("Digite 999 para sair.")
c = s = 0
while True:
    n = int( input( " Digite um número: " ) )
    if n == 999:
        break
    c += 1
    s += n
print(f" Foram digitados {c} números.\n Soma destes é {s}.")