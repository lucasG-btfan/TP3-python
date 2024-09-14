# Ejercicio 3: Suma de Cada Fila
# Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional.

matriz = [
    [1, 2, 3], # 6
    [4, 5, 6], # 15
    [7, 8, 9] # 24
]

suma_total = sum(sum(fila) for fila in matriz)
print(f"la suma total es: {suma_total}")

for fila in matriz:
    print(f"La suma de los elementos en la fila: {fila} es {sum(fila)}")

