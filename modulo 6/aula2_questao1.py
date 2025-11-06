import random

# Gera 20 números inteiros entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Exibe resultados
print("Lista ordenada:", sorted(lista))
print("Lista original:", lista)
print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))
