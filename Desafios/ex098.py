from time import sleep

def l(cor):
    cores = ['oi']
    for r in range(1,7):
        cores.append(f'\033[3{r}m')
    print(cores[cor],'_'*36,'\033[m')

def cont(ini,fim,con):
    
    if con == 0:
        con = 1
    if con < 0:
        con *= (-1)
    
    l(2)
    print(f' Contagem de {ini} a {fim} de {con} em {con}.')
    l(2)
    
    sleep(3)
    
    l(4)
    c = ini
    
    if ini < fim:
        while c <= fim:
            print(f' {c}', end = ' ', flush = True)
            sleep(0.5)
            c += con
        print('Fim!!')
    
    else:
        while c >= fim:
            print(f' {c}', end = ' ',flush = True)
            sleep(0.5)
            c -= con
        print('Fim!!')
    l(4)
    sleep(2)    


cont(1,10,1)
cont(10,0,2)

l(3)
x = int( input(' Início: '))
y = int( input(' Fim: '))
z = int( input(' Condição: '))
l(3)

cont(x,y,z)