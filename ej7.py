arreglo_usuario = (input("Ingrese una lista de números separados por espacios: "))
arreglo_cadena = arreglo_usuario.split()
arreglo_numeros = [int(i) for i in arreglo_cadena]
suma = sum(arreglo_numeros)
promedio = suma / len(arreglo_numeros)
print("El promedio es: ", promedio)
