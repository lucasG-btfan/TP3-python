fyc = int(input("Ingrese la cantidad de filas y columnas: "))

# Crear la matriz de identidad inversa
identidad_inversa = [[1 if j == fyc - i - 1 else 0 for j in range(fyc)] for i in range(fyc)]

# Imprimir la matriz de identidad inversa
for fila in identidad_inversa:
    print(fila)
