nome = str(input("Digite seu nome completo: "))

print(f"Maiúsculas: {nome.upper()}")
print(f"Minúsculas: {nome.lower()}")
print("Número de letras: ", len(nome.replace(" ", "")))
print(len(nome.split()[0]))