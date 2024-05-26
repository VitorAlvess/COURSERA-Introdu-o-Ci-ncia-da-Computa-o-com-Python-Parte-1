

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável para armazenar a soma dos dígitos
soma_dos_digitos = 0

# Converte o número para uma string para iterar sobre cada dígito
for digito in str(numero):
    # Converte cada caractere de volta para inteiro e soma
    soma_dos_digitos += int(digito)

# Imprime a soma dos dígitos
print(soma_dos_digitos)