casa = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe o salário do comprador: R$'))
ano = int(input('Em quantos anos você deseja pagar? '))

mensal = casa / (ano * 12)
porcentagem = sal * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos', end='') 
print(f' a prestação será de R${mensal:.2f}')

if mensal <= porcentagem:
    print('O Empréstimo foi \033[32mAPROVADO!\033[m')
else:
    print('O Empréstimo foi \033[31mNEGADO!\033[m')
