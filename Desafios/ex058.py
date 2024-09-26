from random import randint
from time import sleep

pc = randint(0, 10)
player = -1
graça = ["Aposto que vai errar", " Errou de novo? ", "Pode desistir rsrs"]
c = 0
cores = ["\033[36m", "\033[34m", "\033[35m", "\033[32m", "\033[33m", "\033[31m"]

print("Consegue adivinhar meu número? ")

while player != pc:
    
    j = randint(0,2)   
    g = randint(0,2)
    
    if c > 0:
        sleep(3)
        print(cores[j], graça[g], "\033[m")
                
        if pc > player:
            print("{} Mais alto..{}".format(cores[j], "\033[m" )) 
        else:
            print("{} Mais baixo..{}".format(cores[j], "\033[m" ) )

    print("") 
    player = int( input("Digite seu palpite: " ) )
    print("")
    print(" Processando... ")
    print("")
    
    sleep(3)
    
    c += 1
    
if c < 4:
    cor = cores[3]
elif c > 6:
    cor = cores[5]
else:
    cor = cores[4]

if player == pc:
    print("{}Você tentou {} vezes até acertar.{}".format(cor, c, "\033[m"))