c = 0
fim = "\033[m"
while True:  
    tabu = int( input("Qual Tabuada? ") )
    if tabu < 0:
        break
        
    for ta in range (0, 11):
        if c % 2 == 0:
            cor = "\033[35m"
        else:
            cor = "\033[36m"
        print("{}{}x{:2} = {}{}".format(cor,tabu,ta,tabu*ta,fim))
        c += 1
