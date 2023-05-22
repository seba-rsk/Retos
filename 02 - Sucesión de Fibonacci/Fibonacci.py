# Genero una lista vacía para almacenar los valores de la serie.
serie = []

for x in range(50):
    if x == 0 or x == 1:
        serie.append(x)
    else:
        # Almaceno en la lista 'serie' la suma de los últimos dos números de la serie almacenados.
        serie.append(serie[-1] + serie[-2])

for i, n in enumerate(serie):
    print(i+1, '-',  n)
