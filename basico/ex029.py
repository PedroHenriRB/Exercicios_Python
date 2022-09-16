from time import sleep

vel = float(input('Qual é a velocidade atual do carro? '))

print('CARREGANDO...')
sleep(2)

if vel > 80:
    print(f'VOCÊ FOI MULTADO! você passou do limite de velocidade. \nVocê deve pagar uma multa de R${(vel - 80) * 7:.2f}')
print('Tenha um bom dia.')
# Quando não se utiliza o else é chamado de condição simples.
