#Creamos variable que tome el valor de filas y colunmnas
fyc=int(input("Ingrese la catidad de filas y columnas: "))
#Creamos la matriz identidad
identidad = [[1 if i == j else 0 for j in range(fyc)] for i in range(fyc)]
#mostramos en pantalla el resultado
for fila in identidad:
 print(fila)
