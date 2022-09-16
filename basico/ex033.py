num1 = int(input('Digite três números\n'))
num2 = int(input())
num3 = int(input())

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O menor valor digitado foi {menor}')

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O maior valor digitado foi {maior}')
