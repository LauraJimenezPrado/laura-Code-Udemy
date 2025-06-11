
"""ingreso del usuario"""
texto = input("Ingresa un texto de al menos 10 palabras: ")

"""contar el numero total de caracteres en el texto"""
num_caracteres = len(texto)
print(num_caracteres)

"""contar el numero de caracteres sin contar los espacios"""
num_espacios = texto.count(" ")
num_catacteres_sin_espacios = num_caracteres - num_espacios
print(num_espacios)

"""contar la cantidad de vocales que hay en un texto"""
num_a = texto.count("a")
num_e = texto.count("e")
num_i = texto.count("i")
num_o = texto.count("o")
num_u = texto.count("u")
num_vocales = num_a + num_e + num_i + num_o + num_u
print(num_vocales)


"""contar el numero total de palabras en el texto ingresado"""
num_palabras = num_espacios + 1
print(num_palabras)

"""eliminar la primera palabra"""
primer_espacio =texto.find(" ")
sin_primera_palabra = texto[primer_espacio + 1:]
print(sin_primera_palabra)

"""Reemplazar todos los espacios por guines medios"""
guiones = texto.replace(" ", "-")
print(guiones)

"""cambia las mayusculas a minusculas y las minusculas a mayusculas"""

viceversa = texto.swapcase()
print(viceversa)


"""muestrale al usuario los resultados"""

print(f"El numero de caracteres es {num_caracteres}")
print(f"Y si no contamos los espacios tienes {num_catacteres_sin_espacios} catacteres")
print(f"De los caracteres de texto, hay {num_vocales} que son vocales")
print(f"Si contamos las palabras, tu texto tiene {num_palabras} palabras")
print(f"Eliminando la primera palabra, queda así {sin_primera_palabra}")
print(f"Si cambiamos espacios por guiones, se ve así {guiones}")
print(f"Cambiando mayusculas por minusculas, queda: {viceversa}")
