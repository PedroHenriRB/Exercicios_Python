from random import randint
from time import sleep      #Espera o tempo que o usuário comandar

num = int(input('Adivinhe um número de 0 a 5 que o computador está pensando: '))
com = randint(0, 5)

print('CARREGANDO...')
sleep(2)

if com == num:
    print(f'Você escolheu o mesmo número que ele. \nPARABÉNS, VOCÊ GANHOU!')
else:
    print(f'Você ERROU o número. \nTENTE OUTRA VEZ!')
