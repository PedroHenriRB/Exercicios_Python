frase = str((input("Digite uma frase: "))).strip().lower()

print(f"A letra \"a\" aparece {frase.count('a')} vezes.")
print(f"Posição primeira vez: {frase.find('a')}")
print("Posição última vez: ", frase.find('a'))