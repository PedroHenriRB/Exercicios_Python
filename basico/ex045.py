from random import randint
from time import sleep

print('\033[35mVamos jogar JOKENPO ?\033[m')
sleep(1)

itens = ('Pedra', 'Papel', 'Tesoura')

print('''Escolha:
[ 0 ] Pedra.
[ 1 ] Papel.
[ 2 ] Tesoura.''')

com = randint(0, 2)
jogador = int(input('Jogador: '))

if jogador >= 3:
    print('\033[1;31mOpção Inválida. Tente novamente!\033[m')
    quit()

print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!\033[m')
sleep(1)



print('=-' * 10)
print(f'\033[31mCOMPUTADOR\033[m: {itens[com]}')
print(f'\033[32mJOGADOR\033[m: {itens[jogador]}')
print('=-' * 10)
sleep(1)

if jogador == 'Pedra' and com == 'Tesoura':
    print('\033[1;32mPARABÉNS!!! você venceu.\033[m')
elif jogador == 'Papel' and com == 'Pedra':
    print('\033[1;32mPARABÉNS!!! você venceu.\033[m')
elif jogador == 'Tesoura' and com == 'Papel':
    print('\033[1;32mPARABÉNS!!! você venceu.\033[m')
elif jogador == com:
    print('\033[33mEMPATE! tente novamente.\033[m')
else:
    print('\033[1;31mVOCÊ PERDEU!!! tente novamente.\033[m')
