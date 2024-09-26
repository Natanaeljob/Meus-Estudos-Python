from random import randint
op = n = 0
c = 0
while True:
    print("=~"*18)
    
    op = str( input(" Par ou Ímpar? ") ).lower().strip()
    print("=~"*18)
    pc = randint(0,9)
    player = int( input( " Digite um número: " ) )
    n = player + pc
    
    print("=~"*18)

    if n % 2 == 0 and op == "par":

        print("Você me venceu!!\n" if c < 1 else " Venceu de novo, muito bem !!!\n")
        print("=~"*18)
        print(f"Eu escolhi {pc} e você escolheu {player} \n")
        print(f"{n} é par\n")

    elif n % 2 != 0 and op == "impar":
        
        print("Você me venceu!!\n" if c < 1 else " Venceu de novo, muito bem !!!\n")
        print(f"Eu escolhi {pc} e você escolheu {player} \n")
        print("=~"*18)
        print(f"{n} é ímpar\n")

    
    else:
        
        print("Eu venci você!!\n")
        print(f"Eu escolhi {pc} e você escolheu {player} \n")
        print("=~"*18)
        print(f"{n} é par." if n % 2 == 0 else f"{n} é ímpar.\n" )
        break
    c += 1

print("=~"*18)
print(f"\nVenceu o computador {c} vezes!!!")