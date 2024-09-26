boletim = dict()

boletim['Nome'] = str(input(' Nome: ')).upper().strip()
boletim['média'] = float(input(' Média: '))

if boletim['média'] < 5:
    boletim['situação'] = 'Reprovado'

elif 5 <= boletim['média'] < 7:
    boletim['situação'] = 'Recuperação'

else:
    boletim['situação'] = 'Aprovado'

for v, k in boletim.items():
    print(f'{v}: {k}')