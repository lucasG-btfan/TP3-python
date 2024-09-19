"""Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud."""

orden_listas=int (input("Ingresa el numero que indica cuantos elementos tienen las dos listas"))
elemenetos_1 = input(f"Ingresa una lista de {orden_listas}números separados por espacios: ")
lista_1 = list(map(int,elemenetos_1.split()))
elemenetos_2 = input(f"Ingresa una lista de {orden_listas} números separados por espacios: ")
lista_2 = list(map(int,elemenetos_2.split()))

lista_3=[]
i=0
while i < orden_listas:
  lista_3.append(lista_1[i] + lista_2[i])
  i+=1
print (lista_3)
