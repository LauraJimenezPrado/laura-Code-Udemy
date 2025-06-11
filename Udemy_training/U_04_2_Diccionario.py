"""los diccionarios es hacen con corchetes {}
los componen un elemento clave y un valor"""

diccionario_ejemplo ={}
print(type(diccionario_ejemplo))

edades = {"Juan":25 , "Maria":32}
print(edades)


"no pueden haber claves que no tengan valor y no pueden haber valores que no tengan claves"""

"""aquí tambien puedo aplicar LEN para conocer el tamaño de una coleccion"""

"""va decir 2"""
print(len(edades))

"""los diccionarios no se pueden indexar porque no tienen un orden establecido
si yo imprimo 
print(edades[0])
va aparecer un error, porque no son secuencias de elementos"""

"""va imprimir la edad de Juan"""
print(edades["Juan"])

edades["Juan"] = 26
print(edades)
"""{'Juan': 26, 'Maria': 32} porque actualiza la edad de Juan"""

"Ahora para agregar elementos"

edades["Laura"] = 28
print(edades)
"""{'Juan': 26, 'Maria': 32, 'Laura': 28}"""

dir(edades)

print(edades.keys())
"""dict_keys(['Juan', 'Maria', 'Laura'])"""

print(edades.values())
"""dict_values([26, 32, 28])"""

"""ahora va imprimir una tupla con todos los items"""
print(edades.items())
"""dict_items([('Juan', 26), ('Maria', 32), ('Laura', 28)])"""


print(edades.get("Juan"))
"""imprime 26 , get ayuda a traer una info por una especie de indexación"""

edades.update({"Juan":30})
print(edades)
"""{'Juan': 30, 'Maria': 32, 'Laura': 28}"""
"""se actualizo la edad"""


"""Ejercicio Diccionarios en Python 1
Crea un diccionario llamado mi_diccionario que contenga los siguientes tres pares de clave-valor, donde las claves sean los nombres de tres  frutas, y los valores sean su color principal.

Los pares clave-valor que guardarás en tu diccionario son los siguientes:
"manzana" - "roja",
"banana" - "amarilla",
"naranja" - "naranja"""


mi_diccionario = {
    "manzana": "roja",
    "banana": "amarilla",
    "naranja": "naranja"
}

print(mi_diccionario)


"""Ejercicio Diccionarios en Python 2
Dado el siguiente diccionario edades, que asocia nombres de personas con su edad: edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
Realiza las siguientes tareas: 

Accede a la edad de Elena e imprímela.
Modifica la edad de Juan a 29 años e imprime el resultado.
Añade un nuevo par clave-valor, asociando a "Luisa" con 25 años e imprime el diccionario completo actualizado."""

edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
print("Edad de Elena:", edades["Elena"])
edades["Juan"] = 29
print("Edad actualizada de Juan:", edades["Juan"])
edades["Luisa"] = 25
print("Diccionario actualizado:", edades)



"""Ejercicio Diccionarios en Python 3
Con el siguiente diccionario productos que contiene productos como claves y sus precios como valores: 
productos = {"manzana": 0.40, "banana": 0.50, "cereza": 0.80}

Realiza las siguientes operaciones usando métodos apropiados de diccionarios: 

Guarda todas las claves del diccionario en una variable, e imprímela.
Guarda todos los valores del diccionario en una variable, e imprímela.
Añade un nuevo producto llamado "naranja" con un precio de 0.60. Imprime el resultado
Actualiza el precio de la "banana" a 0.75. Imprime el resultado
Imprime todos los pares clave-valor del diccionario actualizado.
"""
productos = {"manzana": 0.40, "banana": 0.5, "cereza": 0.80}

claves = productos.keys()
print(claves)

valores = productos.values()
print(valores)

productos["naranja"] = 0.60
print(productos)

productos["banana"] = 0.75
print(productos)

print(productos.keys(), productos.values())


