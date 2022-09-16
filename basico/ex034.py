salario = float(input('Qual é o salário do funcionário? R$'))

aumento10 = salario * 10 / 100
aumento15 = salario * 15 / 100

if salario > 1250:
    print(f'Quam ganhava R${salario:.2f} passou a ganhar R${salario + aumento10:.2f} agora.')
else:
    print(f'Quem ganhava R${salario:.2f} passou a ganhar {salario + aumento15:.2f} agora.')
