# Ejercicio 3: Invertir una Lista
# Escribe un programa que permita al usuario ingresar una lista y la invierta.
i = int(input("ingresa la cantidad de elementos que quieres en la lista "))
arreglo = []

for n in range(0, i):
    arreglo.append(input(f"ingresa el valor de la posicion {n}: "))

arreglo.reverse()

print(arreglo)