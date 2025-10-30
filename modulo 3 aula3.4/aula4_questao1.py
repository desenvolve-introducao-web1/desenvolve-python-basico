# aula4_questao1.py
# Programa que lê dois números e informa se a soma é par ou ímpar

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

if soma % 2 == 0:
    print(f"A soma é {soma} e é PAR.")
else:
    print(f"A soma é {soma} e é ÍMPAR.")
