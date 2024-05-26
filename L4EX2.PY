

def e_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def maior_primo(n):
    for num in range(n, 1, -1):
        if e_primo(num):
            return num

# Exemplos de uso:
maior_primo(10)


