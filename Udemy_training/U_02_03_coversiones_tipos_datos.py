"""convertir un tipo de de dato en otro tipo de dato se llama casting 

existen dos tipos de cambios

1. implicitas: Python convierte el tipo de datos en otro tipo de datos automaticamente. En este proceso el usuario no debe hacer nada
2. explicitas: Python necesita que el usuario haga algo para convertir un tipo de dato en otro 

"""

mi_valor = 1
print(mi_valor)
print(type(mi_valor))

otro_valor = str(mi_valor)
print(otro_valor)
print(type(otro_valor))



num1 = 20
num2 = 30.56

print(type(num1)) 
"""es un int """

print(type(num2)) 
""" es un float """


num1 = num1 + num2
print(type(num1))
"""ahora es un float"""

print(type(num2))

num_new = 5.98
print(num_new)
print(type(num_new))


num_new_2 = int(num_new)
print(num_new_2)
print(type(num_new_2))


edad = input("dime tu edad: ")
edad = int(edad)
nueva_edad = 1 + edad
print(nueva_edad)
print(type(nueva_edad))


num2 = 10
num2 = float(num2)
print(type(num2))


num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))