#Escribe un programa que permita al usuario ingresar una lista de números y eliminar
#un elemento en un índice especificado.
numeros = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(int,numeros.split()))
indice= int(input ("Ingresa un índice"))
del lista_numeros[indice]
print(lista_numeros)
