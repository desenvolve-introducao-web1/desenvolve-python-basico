# aula1_questao5.py
N = int(input("Digite a quantidade de pessoas: "))
soma = 0

for i in range(N):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma += idade

media = soma / N
print(f"Média das idades: {media:.2f}")
