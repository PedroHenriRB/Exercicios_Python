lar = float(input("Digite a largura: "))
alt = float(input("Digite a altura: "))
area = lar * alt 

print(f"Sua parede tem a dimensão de {lar}x{alt} e sua área é de {area}m².")
print(f"Para pintar a sua parede, você precisará de {area / 2:.2f}l de tinta")
