p1 = float( input( " Altura em m. " ) )
p2 = float( input( " Largura em m. " ) )
t = float( input( "\033[36m Rendimento da tinta por litro\033[m" ) )
area = p1 * p2
calculo = area / t

print( " São necessários {}{}{}L de tinta para pintar {} m. ".format( "\033[36m",calculo,"\033[m",area ) )