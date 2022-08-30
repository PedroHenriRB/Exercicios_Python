nome = str(input("Digite seu nome completo: "))

print(f"Maiúscula: {nome.upper()}")
print(f"Minúscula: {nome.lower()}")
print("Números de letras: ", len(nome.replace(" ", "")))

print(len(nome.split()[0]))