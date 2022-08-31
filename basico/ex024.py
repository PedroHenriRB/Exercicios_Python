cidade = str(input("Em que cidade você nasceu: ")).upper().replace("-"," ").split()

print("SANTO" in cidade[0:6])