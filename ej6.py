cantidad=int(input("Cuantos numeros desea ingresar? "))
arreglo=[]
numero=0
i=0
for i in range (1,cantidad+1):
    numero=int(input(f"Diga el numero en la posicion {i}: "))
    arreglo.append(numero)
arreglo=set(arreglo)
for i in arreglo:
    print (i)
print("Los numeros repetidos fueron eliminados")        
