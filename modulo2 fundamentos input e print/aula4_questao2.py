# Lê o valor em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte para Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Converte o valor de Celsius para inteiro
celsius_inteiro = int(celsius)

# Exibe a mensagem formatada
print(f"{fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius.")
