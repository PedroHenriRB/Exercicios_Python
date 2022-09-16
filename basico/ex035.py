s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODE FORMAR um triângulo.')
