n = int(input("Digite um número natural: "))
def fatorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicita ao usuário que insira um número natural

# Calcula e imprime o fatorial de n
print(fatorial(n))