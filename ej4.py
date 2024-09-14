# Ejercicio 4: Contar Elementos Pares e Impares
# Escribe un programa que pida al usuario una lista de números y cuente cuántos de ellos son pares y cuántos son impares.

arreglo = []
pares = 0
impares = 0

for n in range(0, 5):
    numero = int(input(f"ingresa el valor de la posicion {n}: "))
    if numero % 2 == 0:
        pares += 1
    else :
        impares += 1
    arreglo.append(numero)

print(f"La lista es: {arreglo}")
print(f"Impares: {impares}")
print(f"Pares: {pares}")
