palavras = ("amora","maça","banana","couve","uva","laranja","caju","goiaba","framboesa")
c = ' '
t = 0
for frutas in palavras:
    print('')
    if t % 2 == 0:
        c = '\033[35m'
    else:
        c = '\033[34m'
        
    print(f'{c}A palavra {frutas.upper()} tem as vogais: ' , end = ' ')
    
    for l in frutas:
        if l.lower() in 'aeiou' :
            print(l, end = '')
    t += 1