arreglo = [3, 6, 9, 12, 15]
multiplicador = int(input("Ingrese un número: "))
for i in range(0,5):
    resultado = multiplicador * arreglo[i]
    print(f"{arreglo[i]} x {multiplicador} = {resultado}")
