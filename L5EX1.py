largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

for i in range(altura):  # Itera sobre as linhas do retângulo
    for j in range(largura):  # Itera sobre as colunas do retângulo
        print("#", end="")  # Imprime um caractere '#' sem quebra de linha
    print()  # Imprime uma quebra de linha após cada linha do retângulo
