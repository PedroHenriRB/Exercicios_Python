"""
co = float(input("Digite o cateto oposo: "))
ca = float(input("Digite o cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"O valor da hipotenusa é {hi:.2f}")
"""
# Resolvendo com a biblioteca math

from math import hypot

co = float(input("Digite o cateto oposo: "))
ca = float(input("Digite o cateto adjacente: "))
hi = hypot(co, ca)

print(f"O valor da hipotenusa é: {hi:.2f}")