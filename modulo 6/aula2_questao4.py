# Entrada da primeira lista
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(n1)]

# Entrada da segunda lista
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(n2)]

# Criação da lista intercalada
lista_intercalada = []
for i in range(max(n1, n2)):
    if i < n1:
        lista_intercalada.append(lista1[i])
    if i < n2:
        lista_intercalada.append(lista2[i])

print("Lista intercalada:", lista_intercalada)
