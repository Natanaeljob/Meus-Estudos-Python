jog = ( " ", "Athletico-PR", "Atlético-GO", "Atlético-MG", "Bahia", "Botafogo", "Corinthians", "Criciúma", "Cruzeiro", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Grêmio", "Internacional",
"Juventude", "Palmeiras", "Bragantino", "São Paulo", "Vasco da Gama", "EC Vitória" )

print(f' Os 5 primeiros colocados são:\n{jog[1:5]}.')
print("")
print(f' Os 4 últimos colocados são: {jog[-4:]}.')
print("")
print(f' Todos os times: {sorted(jog[1:])}')
print("")
print(' Palmeiras está na {}ª posição'.format(jog.index('Palmeiras') ) )