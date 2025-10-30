# aula4_questao4.py
# Calcula o valor do frete conforme a distância e peso do pacote

distancia = float(input("Digite a distância em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0

valor_frete = preco_por_kg * peso

if peso > 10:
    valor_frete += 10  # taxa adicional

print(f"O valor total do frete é: R${valor_frete:.2f}")
