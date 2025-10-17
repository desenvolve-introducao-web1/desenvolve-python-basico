# Produto 1
nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input(f"Digite o preço unitário do produto 1:{nome1} "))
quant1 = int(input(f"Digite a quantidade do produto 1:{nome1} "))

# Produto 2
nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input(f"Digite o preço unitário do produto 2:{nome2} "))
quant2 = int(input(f"Digite a quantidade do produto 2:{nome2} "))

# Produto 3
nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input(f"Digite o preço unitário do produto 3:{nome3} "))
quant3 = int(input(f"Digite a quantidade do produto 3:{nome3} "))

# Calcula o total da compra
total = (preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3)

# Exibe o total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
