class asignarArreglo:
    def llenarlo(self, a, b):
        for i in range(b):
            valor = float(input(f"Ingrese el valor {i + 1}: "))
            a.append(valor)

    def sumarLista(self, a, b):
        if len(a) != len(b):
            print("Las listas no tienen la misma longitud.")
            return
        d = [a[i] + b[i] for i in range(len(a))]
        print("La suma de las listas es:", d)

def igualdad(x, y):
    if x == y:
        lista = []
        lista2 = []
        asignar = asignarArreglo()
        asignar.llenarlo(lista, x)
        asignar.llenarlo(lista2, y)
        asignar.sumarLista(lista, lista2)
    else:
        print("ERROR: los valores de las listas no son iguales.")
        x = int(input("Ingrese el número de valores de la primera lista: "))
        y = int(input("Ingrese el número de valores de la segunda lista: "))
        igualdad(x, y)

listadenum1 = int(input("Ingrese el número de valores de la primera lista: "))
listadenum2 = int(input("Ingrese el número de valores de la segunda lista: "))

# Confirmamos si su longitud es igual
igualdad(listadenum1, listadenum2)
