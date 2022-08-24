km = float(input("Quantidades de Km rodados? "))
dia = int(input("Quantidade de dias alugados? "))

pagardia = dia * 60
pagarkm = km * 0.15

print(f"Total a pagar R${pagardia + pagarkm:.2f}")