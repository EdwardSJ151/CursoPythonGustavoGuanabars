frase = str(input("Digite uma frase: ")).strip().lower()
print(f'A letra A aparece {frase.count("a")}')
print(f'A primeira letra A apareceu na posicão {frase.find("a")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("a")+1}')
