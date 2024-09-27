filas = 3
columnas = 3

tabla = [
    [1, 5, 0], 
    [4, 1, 3], 
    [0, 6, 1]
]

for fila in tabla:
    print(fila)

tabla90grados = [[0 for _ in range(filas)] for _ in range(columnas)]

for j in range(filas):
    for i in range(columnas):
        tabla90grados[i][filas - 1 - j] = tabla[j][i]


print("La tabla girada 90 grados en el sentido de las agujas del reloj es de esta manera:")
for fila in tabla90grados:
    print(fila)