matriz = [[3, 6, 2], [1, 9, 5], [7, 4, 8]]
mayor = matriz[0][0] # Se puede utilizar cualquier valor de la matriz, en este caso utilizo el 1ro
for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        if matriz[i][j] >= mayor:
            mayor = matriz[i][j]

print(mayor)
