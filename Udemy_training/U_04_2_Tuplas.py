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

