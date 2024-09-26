def notas(*media, sit = False):
    '''
    Mostra a média da turma
    
    :param média: insira as médias utilizando ',' para separar.
        
    :param sit:(opcional) insira sit=True para ver a situação da turma.
        
    :return: retorna um dicionário com os dados da turma.
    '''
    ordem= dict()
    maior = menor = med = 0
    ordem['Total'] = len(media)
    for o in media:
        med += o
        if maior == 0:
            maior = o
            ordem['maior nota'] = o
        elif maior < o:
            maior = 0
            ordem['maior nota'] = o
        if menor == 0:
            menor = o
            ordem['menor nota'] = o
        elif menor > o:
            menor = o
            ordem['menor nota'] = o
    med = med / len(media)
    #i = max(media) metodo simples de pegar o maior de uma lista
    ordem['Média T.'] = float(f'{med:.1f}')
    
    if sit:
        if med >= 8: 
            tip = 'Ótima'
        elif med >= 6:
            tip = 'Razoável'
        elif med >= 5:
            tip = 'Ruim'
        else:
            tip = 'Muito ruim'
    
        ordem['Situação'] = tip
    return ordem


resp = notas(9.7,7.4,8.2,5.3,9.1,sit=True)

for v, k in resp.items():
    print(f'{v}: {k}')
print(help(notas))