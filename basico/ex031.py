from time import sleep

viagem = float(input('Informe a distância da viagem: '))

print('CARREGANDO O VALOR DA PASSAGEM...')
sleep(2)

if viagem <= 200:
    print(f'O valor da passagem é R${viagem * 0.50:.2f}')
else:
    print(f'O valor da passagem é R${viagem * 0.45:.2f}')