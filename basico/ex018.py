"""
import math

angulo = float(input("Digite um ângulo: "))
sen = math.sin(math.radians(angulo))
con = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O ângulo de {angulo} tem SENO de: {sen:.2f}")
print(f"O ângulo de {angulo} tem COSSENO de: {con:.2f}")
print(f"O ângulo de {angulo} tem TANGENTE de: {tan:.2f}")
"""

from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {angulo} tem SENO de: {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de: {cosseno:.2f}")
print(f"O ângulo de {angulo} tem TANGENTE de: {tangente:.2f}")