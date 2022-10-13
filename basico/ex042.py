a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os segmentos \033[32mFORMAM\033[m um Triângulo ',end='')
    if a == b == c:
        print('Equilátero.')
    elif a == b or a == c or b == c:
        print('Isósceles.')
    elif a != b != c != a:
        print('Escaleno.')
else:
    print('Os segmentos \033[31mNÃO FORMAM\033[m um Triâgulo.')
