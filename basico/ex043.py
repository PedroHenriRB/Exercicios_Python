alt = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (alt ** 2)

print(f'Você tem {alt} de altura e {peso}kg, seu IMC é: {imc:.1f}')

if imc < 18.5:
    print('Você está \033[31mABAIXO DO PESO\033[m normal.')
elif imc >= 18.5 and imc < 25:
    print('Você está com o \033[32PESO IDEAL\033[m.')
elif imc >= 25 and imc < 30:
    print('Você está com \033[33mSOBREPESO\033[m.')
elif imc >= 30 and imc < 40:
    print('Você está com \033[31mOBESIDADE\033[m.')
elif imc >= 40:
    print('Você está com \033[1;31mOBESIDADE MÓRBIDA!!!\033[m')

