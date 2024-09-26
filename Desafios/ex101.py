from função import *

def testvoto(ano):
    from datetime import date
    anoa = date.today().year
    idade = anoa - ano
    ls('_',5)
    print(f' Idade {idade} anos: ', end = '')
    if idade < 16:
        pc('Não Vota',2)
    elif idade < 18 or idade > 60:
        pc('Voto Opcional',3)
    else:
        pc('Voto Obrigatório!!',1)


lc('Devo votar ?','_',3,5)
print('')
testvoto(int(input('Digite seu ano de Nascimento: ')))
ls('_',5)