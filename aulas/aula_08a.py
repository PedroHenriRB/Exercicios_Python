# Utilizando Módulos

import math         #Importa a biblioteca math(CTRL + Espaço aparece todos os módulos).

num = int(input("Digite um número: "))
raiz = math.sqrt(num)                                           #sqrt = raiz quadrada

print(f"A raiz de {num} é igual a {math.floor(raiz)}.")          #ceil/floor = arredonda um número para cima/arredonda pra baixo
                                                                 