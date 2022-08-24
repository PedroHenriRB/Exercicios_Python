salario = float(input("Informe o salário do funcionário: "))
aumento = salario * 15 / 100
novo = salario + aumento

print(f"O novo salário do funcionário com 15% de aumento é R${novo:.2f}")