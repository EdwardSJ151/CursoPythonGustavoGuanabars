frase = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maíusculo é {frase.upper()}.')
print(f'Seu nome em minúsculo é {frase.lower()}.')
print(f'Seu nome ao todo tem {len(frase) - frase.count(" ")} letras.')
# print(f'Seu primeiro nome é tem {frase.find(" ")} letras.')
separa = frase.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
