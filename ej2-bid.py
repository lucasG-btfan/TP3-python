fila = int(input("Ingrese el número de filas: "))
columna = int(input("Ingrese el número de columnas: "))

matriz = []
for i in range(fila):
    # Creamos un arreglo para generar las filas
    filas = []
    for j in range(columna):
        valor = int(input(f"Ingrese el valor de la matriz[{i+1}][{j+1}]: "))
        filas.append(valor)
    matriz.append(filas)

# Imprimir la matriz para verificar
print("Matriz ingresada:")
for fila in matriz:
    print(fila)

# Calcular la suma total de los elementos de la matriz
suma_total = sum(sum(fila) for fila in matriz)
print(f"La suma total de los elementos de la matriz es: {suma_total}")
