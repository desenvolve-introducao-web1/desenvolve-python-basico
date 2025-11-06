
# aula1_questao2.py
# Gera n números aleatórios e calcula a raiz quadrada da soma

import random
import math

n = int(input("Digite a quantidade de números aleatórios: "))

soma = 0
for i in range(n):
    numero = random.randint(0, 100)
    soma += numero
    print(f"Número gerado: {numero}")

raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma dos valores é: {raiz:.2f}")
