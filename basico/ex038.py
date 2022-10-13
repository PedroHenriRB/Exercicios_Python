num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('O \033[33mprimeiro valor\033[m é \033[36mmaior\033[m.')
elif num2 > num1:
    print('O \033[33msegundo valor\033[m é \033[36mmaior\033[m.')
elif num1 == num2:
    print('\033[33mNão existe valor\033[m maior, os dois são \033[36miguais\033[m.')
