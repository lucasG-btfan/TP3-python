def encontrar_repetidos(lista):
    repetidos = []
    vistos = set()

    for elemento in lista:
        if elemento in vistos and elemento not in repetidos:
            repetidos.append(elemento)
        vistos.add(elemento)

    return repetidos

# Ejemplo de uso
mi_lista = [1, 2, 3, 2, 4, 5, 1, 6, 3]
elementos_repetidos = encontrar_repetidos(mi_lista)
print("Elementos que se repiten:", elementos_repetidos)
