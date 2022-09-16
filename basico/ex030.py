from time import sleep

num = int(input('Digite um número: '))

print('Seu número é PAR ou ÍMPAR?')
print('CARREGANDO...')
sleep(2)

if num % 2 == 0:
    print(f'O número é PAR.')
else:
    print('O número é ÍMPAR.')
