from datetime import date

ano = int(input('Ano de nascimento: '))
idade = (date.today().year - ano)
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')    

if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento. \nSeu alistamento será em {(18 - idade) + date.today().year}.')
elif idade == 18:
    print(f'Você tem que se alistar \033[1;31mIMEDIATAMENTE!!!\033[m')
else:
    print(f'''Você já deveria ter se alistado há {idade - 18} anos.
Seu alistamento foi em {date.today().year - (idade - 18)}.''')
