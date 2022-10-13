from datetime import date

n = int(input('Ano de Nascimento: '))
idade = date.today().year - n
print(f'O Atleta tem {idade} anos. A categoria dele é:', end=' ')

if idade <= 9:
    print('\033[1;32mMIRIM\033[m.')
elif idade <= 14:
    print('\033[1;32mINFANTIL\033[m')
elif idade <= 19:
    print('\033[1;32mJUNIOR\033[m')
elif idade <= 25:
    print('\033[1;32mSÊNIOR\033[m')
elif idade > 25:
    print('\033[1;32mMASTER\033[1;32m')
