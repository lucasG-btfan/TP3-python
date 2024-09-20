escalar = float(input("Valor escalar: "))

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = [[elemento * escalar for elemento in fila] for fila in matriz]

print("Matriz escalada:")

for fila in resultado:
    print(fila)
