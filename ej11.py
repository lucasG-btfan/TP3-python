numdlista = int(input("Ingrese el número de valores de la lista: "))
lista = []

# Ingresaremos los valores del arreglo
for i in range(numdlista):
    valor = float(input(f"Ingrese el valor {i + 1}: "))
    lista.append(valor)

print("Tu lista es:", lista)
