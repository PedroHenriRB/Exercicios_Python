preco1 = float(input("Digite o preço do produto: "))
desconto = preco1 * (5 / 100)
preco2 = preco1 - desconto

print(f"O produto que custava R${preco1}, na promoção de 5% vai custar R${preco2:.2f}")