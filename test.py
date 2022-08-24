frase1 = input("Digite uma frase: ")
frase2 = input("Digite uma frase: ")

print(f"String 1: {frase1}")
print(f"String 2: {frase2}")

print(f"Tamanho de \"{frase1}\":", len(frase1))
print(f"Tamanho de \"{frase2}\":", len(frase2))

if len(frase1) == len(frase2):
    print("As duas Strings são de tamanhos iguais.")
else:
    print("As duas Strings são de tamanhos diferentes.")

if frase1 == frase2:
    print("As duas Strings possuem conteúdo iguais.")
else:
    print("As duas Strings possuem conteúdo diferentes.")