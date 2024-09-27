numdlista = int(input("Ingrese el número de valores de la lista: "))
lista = []

# Ingresaremos los valores del arreglo
for i in range(numdlista):
    valor = int(input(f"Ingrese el valor {i + 1}: "))
    lista.append(valor)

print("Tu lista es:", lista)

# lista de numero 

num = int(input('Ingresa un numero para buscar: '))



listaSinRepetir = set(lista)

print(listaSinRepetir)

counter = 0

for j in lista:
    if num == j:
        counter += 1
print("existen " + str(counter) + " elementos de: " + str(num))
    
counter = 0