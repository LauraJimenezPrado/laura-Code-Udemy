"""las tuplas (tuple) son listas pero no se pueden modificar una vez creadas"""

t = 1, 2
print(type(t))

tt = (1, 2)
print(type(tt))

"""acontinuación una tupla mixta """
tm = ("Laura", "Jimenez", 28 )
print(type(tm))


mi_tuple = (1, 3, 5, 7, 9)

print(type(mi_tuple))

elemento_tupla = mi_tuple[2]
print(elemento_tupla)

"""se imprimi el 3 y el 5, inicia a contar en el indice 1 y va hasta el que esta antes del indice 3"""

sub_tupla =mi_tuple[1:3]
print(sub_tupla)

"""si ejecuto lo siguiente: 
mi_tuple[1]= 8

aparece: TypeError: 'tuple' object does not support item assignment 

Porque las tuplas no se pueden modificar"""



print(dir(mi_tuple))  
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']"""

"""va contar cuantas veces esta el numero, por ejemplo el 2, pero aparece 0 veces"""
print(mi_tuple.count(2))

mi_tuple.index(3)

print(mi_tuple.index(3))
"""dice en cual indice esta el numero 3, en este caso esta en el indice 1"""


tupla =(1, 2, 3)
a, b, c =tupla

print(c)

"va aparecer el 3, porque fue el asignado y esa es la manera de desempaquetar las tuplas"


miLista = [1, 2, 3]

a, b, c = miLista
print(c)


"""a continuación una tupla de tuplas"""
nacimiento = (1996, 8, 16)
Nombre =("Laura", "Jimenez")
cliente1 = (Nombre, nacimiento)

print(cliente1)

print(type(cliente1))
print(cliente1[0][1])

auto = ("ford", "fiesta", "rojo", 2021, 5, 1.6)
(marca, tipo, color, modelo, puertas, motor) = auto

print(tipo,puertas)


"""Ejercicio tuplas en Python 1
Crea una tupla llamada mi_primera_tupla que contenga 3 o más elementos de tu preferencia. 
Luego, imprime el segundo elemento de esta tupla."""

mi_primera_tupla = ("laura", "Daniela", "Jimenez", "Prado")
print(mi_primera_tupla[1])

"""Ejercicio tuplas en Python 2
Dada la tupla datos_personales que contiene los siguientes elementos: ("Maria", "Perez", 35, "Ingeniera"), 
utiliza la segmentación de tuplas para imprimir únicamente el nombre y la profesión de María en un mensaje que diga: 
"Maria es Ingeniera".
Para esto puedes crear variables que contengan el nombre y la profesion de Maria según el indice en el que se encuentra 
en la variable datos_personales   Recuerda emplear cadenas lietarles para imprimir el mensaje esperado: "Maria es Ingeniera"""

datos_personales = ("Maria", "Perez", 35, "Ingeniera")
nombre = (datos_personales[0])
profesion= (datos_personales[-1])
print(nombre + " es " + profesion)



"""Ejercicio tuplas en Python 3
Dada una tupla llamada info_ciudades que contiene tres tuplas dentro. Cada tupla interna representa una ciudad y 
contiene el nombre de la ciudad, la población y el país.
("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), ("Tokio", 13929286, "Japón").
Imprime un mensaje para cada ciudad siguiendo el formato siguiente:
"La ciudad de [nombre de la ciudad] en [país] tiene una población de [población] habitantes"

Utiliza los indices requeridos para acceder a los datos especificos de cada pais, crea las variables 
que consideres necesarias y con el empleo de cadenas literales imprime tres mensajes en el orden siguiente:

"La ciudad de Buenos Aires en Argentina tiene una población de 3000000 habitantes"
"La ciudad de Madrid en España tiene una población de 3200000 habitantes"
"La ciudad de Tokio en Japón tiene una población de 13929286 habitantes"""


info_ciudades = (("Buenos Aires", 3000000, "Argentina"), ("Madrid", 3200000, "España"), ("Tokio", 13929286, "Japón"))

ciudad1 = info_ciudades[0]
ciudad2 = info_ciudades[1]
ciudad3 = info_ciudades[2]

print(f"La ciudad de {ciudad1[0]} en {ciudad1[2]} tiene una población de {ciudad1[1]} habitantes")
print(f"La ciudad de {ciudad2[0]} en {ciudad2[2]} tiene una población de {ciudad2[1]} habitantes")
print(f"La ciudad de {ciudad3[0]} en {ciudad3[2]} tiene una población de {ciudad3[1]} habitantes")