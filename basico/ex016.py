import math     #Poderíamos tbm só importar o trunc (from math import trunc).

num = float(input("Digite um número: "))

print(f"O número {num} tem a parte inteira {math.trunc(num)}.")     #trunc = trunca o número na sua forma Inteira

"""
Usando sem a biblioteca math

num = float(input("Digite um número: "))

print(f"O número {num} tem a parte inteira {int(num)})
"""