n1 = float(input('Primeira Nota: '))
n2 = float(input('Segundo Nota: '))
media = (n1 + n2) / 2

print(f'Primeira Nota: {n1} \nSegunda Nota: {n2} \nMédia: {media:.1f}')

if media < 5.0:
    print(f'O aluno está \033[1;31mREPROVADO!\033[m')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de \033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7.0:
    print('\033[36mPARABÉNS!\033[m o aluno foi \033[1;32mAPROVADO!\033[m')