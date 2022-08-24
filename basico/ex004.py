val = (input("Digite algo: "))

print("O tipo primitivo do valor é {}".format(type(val)))

print("Só tem espaços?", val.isspace())
print("É numérico?", val.isnumeric())
print("É alfabético?", val.isalpha())
print("É alfanumérico?", val.isalnum())
print("Está em maiúsculas?", val.isupper())
print("Está em minúsculas?", val.islower())
print("Está capitalizada?", val.istitle())