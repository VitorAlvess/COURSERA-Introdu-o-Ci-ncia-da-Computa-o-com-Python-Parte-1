

def vogal(caractere):
    # Convertendo o caractere para minúsculo para tratar maiúsculas e minúsculas de forma uniforme
    caractere = caractere.lower()
    
    # Verificando se o caractere está na lista de vogais
    if caractere in 'aeiou':
        return True
    else:
        return False

# Exemplos de uso:
vogal("a")
