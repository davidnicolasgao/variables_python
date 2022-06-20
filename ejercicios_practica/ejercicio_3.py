# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())
print('')

# Imprima su nombre completo

print('Tu nombre completo es:', nombre, apellido)
print('')

# Almacenar su nombre completo en una variable
# nombre_completo = .....

nombre_completo = nombre + " " + apellido

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)

print('La cantidad de letras que tiene tu nombre completo es:', len(nombre_completo))
print('')