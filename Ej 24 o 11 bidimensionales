import numpy as np
filas=3
columnas=3
j=0
i=0
tabla=np.array([[0 for _ in range(columnas)] for _ in range(filas)])
for j in range(filas):
    for i in range(columnas):
        tabla[j][i]=int(input(f"Diga el numero de la posicion de fila {j} y la posicion de columna {i} "))

for j in range(filas):
    for i in range(columnas):
        print(f"Valor en la posición ({j}, {i}): {tabla[j][i]}")
tabla90grados=np.rot90(tabla,k=-1)
print("La tabla girada 90 grados en el sentido de las agujas del reloj es de esta manera:")
print (tabla90grados)
