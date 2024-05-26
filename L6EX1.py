def remove_repetidos(lista):
    # Cria um conjunto para armazenar elementos únicos
    conjunto = set(lista)
    # Converte o conjunto de volta para uma lista e a ordena
    lista_sem_repetidos = sorted(list(conjunto))
    return lista_sem_repetidos

# Exemplo de uso:
lista = [4, 2, 5, 2, 8, 4, 9, 5]
resultado = remove_repetidos(lista)
print(resultado)
