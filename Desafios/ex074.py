from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

for re in n:
    print(f' {re}', end = ' ')

print("")
print(f' Maior número sorteado: {max(n)}')

print(f' Menor número sorteado: {min(n)}')