#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float( input( " Digite o ângulo: " ) )

seno = math.sin( math.radians( angulo ) )
pritn( " O ângulo de {} tem o SENO de {:.2f}".format( angulo, seno ) )