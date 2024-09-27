matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
if matriz == transpuesta:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
