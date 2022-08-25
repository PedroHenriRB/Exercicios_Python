from random import choice

aluno1 = input("Digite o 1° aluno: ")
aluno2 = input("Digite o 2° aluno: ")
aluno3 = input("Digite o 3° aluno: ")
aluno4 = input("Digite o 4° aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

print(f"O aluno escolhido foi {choice(lista)}")