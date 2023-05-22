palabra = input('Ingrese la primera palabra: ')

for i in range(len(palabra)):
    if (palabra[i].lower() == palabra[-i-1].lower()):
        continue
    else:
        print('La palabra introducida no es un palíndromo.')
        exit()

print(f'La palabra {palabra} es un palíndromo.')

#Otra forma más sencilla, sería guardando directamente la palaba escrita al revés y luego comparar.

# palabra_rev = palabra[::-1]

# if palabra == palabra_rev:
#     print(f'La palabra {palabra} es un palíndromo.')
# else:
#     print('La palabra introducida no es un palíndromo.')
