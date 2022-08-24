# Há duas maneiras de fazer esse exercício.

num = int(input("Digite um número:"))
print("Seu antecessor é {} e o seu sucessor é {}.".format(num - 1, num + 1))

# E a outra é usar as váriaveis para o antecessor e o sucessor.

ant = num - 1 
suc = num + 1

print(f"Seu antecessor é {ant} e o seu sucessor é {suc}.")