# aula3_questao3.py

import random

# Cria lista de 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontra o intervalo com mais números negativos
# (aqui podemos definir "intervalo" como sequência contínua entre negativos)
maior_seq = []
seq_atual = []
for n in lista:
    if n < 0:
        seq_atual.append(n)
    else:
        if len(seq_atual) > len(maior_seq):
            maior_seq = seq_atual[:]
        seq_atual = []
if len(seq_atual) > len(maior_seq):
    maior_seq = seq_atual[:]

# Remove o primeiro intervalo encontrado
if maior_seq:
    ini = ''.join(map(str, lista)).find(''.join(map(str, maior_seq)))
    i = lista.index(maior_seq[0])
    f = i + len(maior_seq)
    del lista[i:f]

print("Editada:", lista)
