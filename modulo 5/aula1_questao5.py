
# aula1_questao5.py
# Programa que mostra e converte emojis usando a biblioteca emoji

import emoji

print("Emojis disponíveis:")
print("❤️ :red_heart:")
print("👍 :thumbs_up:")
print("🤔 :thinking_face:")
print("🥳 :partying_face:")

frase = input("Digite uma frase e ela será emojizada:\n")

# Converte texto codificado em emoji
frase_emojizada = emoji.emojize(frase)
print("Frase emojizada:")
print(frase_emojizada)
