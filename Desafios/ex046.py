from time import sleep

print("! Contagem regressiva para os fogos !")

print("\n")
sleep(1)

for c in range(10, -1, -1 ):
    print(c)
    sleep(1)
    
print( "\033[31m" + "!!! Os Fogos explodiram !!!" )