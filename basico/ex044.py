print(f'{" Loja Feijão Puro ":=^40}')

preco = float(input('Preço das compras: R$'))
print('''Escolha o método de pagamento:
[ 1 ] À vista dinheiro ou cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até 2x no cartão sem juros.
[ 4 ] 3x ou mais no cartão.''')
metodo = int(input('Escolha: '))
porcent = 10
desconto = preco * porcent / 100

if metodo == 1:
    print(f'Preço do produto à vista: R${preco - desconto:.2f}')
elif metodo == 2:
    porcent = 5
    desconto = preco * porcent / 100
    print(f'Preço do produto à vista no cartão: R${preco - desconto:.2f}')
elif metodo == 3:
    print(f'Preço do produto parcelado em 2x: R${preco / 2:.2f} cada parcela.')
elif metodo == 4:
    parcela = int(input('Quantas parcelas: '))
    porcent = 20
    desconto = preco * porcent / 100
    print(f'Preço do produto parcelado em {parcela}x: R${(preco + desconto) / parcela} cada parcela COM JUROS.')
else:
    print('\033[1;31mMétodo Inválido. Tente novamente.\033[m')