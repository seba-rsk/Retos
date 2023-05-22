palabra1 = input("Ingrese la primera palabra: ").strip().lower()
palabra2 = input("Ingrese la segunda palabra: ").strip().lower()

# Paso a paso:  1 - Convierto a listas las palabras ingresadas, de esta forma cada letra de la palabra introducida es un elemento de la lista.
#               2 - Aplico a cada lista el metodo sorted() que ordena las mismas.
#               3 - Aplico a cada lista ordenada el metodo join() indicando el separador '' para la unión entre los elementos de la lista.
#               4 - Asigo este nuevo string ordenado a una nueva variable que me va a permitir realizar la comparación entre las palabras ingresadas.

palabra1_ord = ''.join(sorted(list(palabra1)))
palabra2_ord = ''.join(sorted(list(palabra2)))

if palabra1_ord == palabra2_ord:
    print('Las palabras ingresadas son anagramas.')
else:
    print('Las palabras ingresadas NO son anagramas.')
