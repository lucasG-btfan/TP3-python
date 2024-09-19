def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Solicitar al usuario que ingrese una lista de números
numeros = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = list(map(int, numeros.split()))

# Filtrar los números primos
numeros_primos = [num for num in lista_numeros if es_primo(num)]

print("Números primos:", numeros_primos)
