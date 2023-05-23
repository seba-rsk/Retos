from math import sqrt

# Salida elegante en caso de que no se ingrese un entero como se solicita.
try:
    n = int(input('Ingrese un número entero:'))
except:
    print('El valor ingresado no corresponde a un número entero.')


def n_primos(num):                  # En lugar de iterar hasta n/2 vamos a iterar hasta sqrt(n), de esta forma reducimos la complejidad de la iteracion de O(n) a O(sqrt(n))
    if abs(num) <= 3:
        return False
    for i in range(2, int(sqrt(abs(num)))+1):
        if num % i == 0:
            return True
    return False


if n_primos(n):
    print('El número no es primo.')
else:
    print('El número es primo.')

input('\'Enter\' para imprimir lista de números primos entre 1 y 100:')
for i in range(101):
    if n_primos(i) == False:
        print(i)
