# aula1_questao6.py
N = int(input())

total = 0
coelhos = 0
ratos = 0
sapos = 0

for _ in range(N):
    linha = input().split()
    quant = int(linha[0])
    tipo = linha[1].upper()
    total += quant
    if tipo == 'C':
        coelhos += quant
    elif tipo == 'R':
        ratos += quant
    elif tipo == 'S':
        sapos += quant

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

print(f"Percentual de coelhos: {(coelhos / total) * 100:.2f} %")
print(f"Percentual de ratos: {(ratos / total) * 100:.2f} %")
print(f"Percentual de sapos: {(sapos / total) * 100:.2f} %")
