import random

# Gera duas listas com 20 inteiros entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Interseção sem duplicatas
interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)
print("\\nContagem:")

for num in interseccao:
    print(f"{num}: (lista1={lista1.count(num)}, lista2={lista2.count(num)})")
