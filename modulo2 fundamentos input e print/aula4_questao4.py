# Lê o valor inteiro em reais
valor = int(input())

# Lista de notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calcula a quantidade de cada nota
for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    print(f"{quantidade} nota(s) de R${nota},00")
