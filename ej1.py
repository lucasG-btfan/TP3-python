cantidad=int(input("Cuantos numeros deseas ingresar? "))
arreglo={}
for i in range(1,cantidad+1):
    arreglo[i]=int(input(f"diga el numero {i} "))
suma=sum(arreglo)
print (f"La suma  de todos los elementos es {suma}")
