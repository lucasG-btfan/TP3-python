# Ejercicio 7: Diagonal de una Matriz Cuadrada
# Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada.
matriz = [
    [1, 2, 3, 4], # 6
    [5, 6, 7, 8], # 15
    [9, 10, 11, 12], # 24
    [13, 14, 15, 16]
]


n = len(matriz)
diagonal = []

for fila in matriz:
     if len(fila) != n:
        raise ValueError("La matriz no es cuadrada")
    
# matriz_diagonal = [matriz[i][i] for i in range(n)]

for i in range(n):
    diagonal.append(matriz[i][i])
    
print(diagonal)

