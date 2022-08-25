peixe = int(input("Digite o kg: "))
excesso = peixe - 50 
multa = excesso * 4

if peixe <= 50:
    print("Nada a pagar")
else:
    print(f"Você dever pagar R${multa} de multa.")