# Solicita ao usuário que insira um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializa uma lista para armazenar os primeiros números ímpares naturais
impares = []

# Loop para encontrar e armazenar os primeiros n números ímpares
for i in range(n):
    impares.append(2 * i + 1)

# Imprime os números ímpares no formato desejado
for numero in impares:
    print(numero)
