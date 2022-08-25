# Utilizando Módulo

from math import sqrt, floor                       #Importa somente o sqrt e floor do Módulo math

num = int(input("Digite um número: "))
raiz = sqrt(num)                            #Como importou somente o sqrt não é necessário usar math.sqrt

print(f"A raiz de {num} é igual a {floor(raiz)}.")

                                            # Para ver todos os módulos do Python(https://docs.python.org/3/library/numeric.html)