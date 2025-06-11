a = True
print(type(a))

"""este tipo es 'bool'  """

b = False
print(type(b))

x = 2
y = 5

print(y == x)

"""va decir falso, recordar que == es para comparar"""

comparar = x==y
print(type(comparar))

"""los operadores booleanos son and, or, not"""


comparar_1 = x < y 
comparar_2 = x > y

"""true"""
print(comparar_1) 

"""false"""
print(comparar_2) 

z = 8

comparar_3 = x < y and y > z
print(comparar_3)

"""si las dos son verdaderas va decir TRUE, si una de las dos es falsa va decir FALSE, 
si las dos son falsas va decir FALSE, si una de las dos es Verdadera pero la otra es falsa va decir FALSE
solo va ser verdadero si todas son verdaderas, así sean muchos operadores"""

"""ejemplo de TRUE con varios operadores"""
comparar_4 = x < y and y < z and x < z and z > y and z > a
print(comparar_4)

"la siguiente dice: Confirmar = print confirmar si no es verdadera, osea si fuera falsa imprimiria verdadero, pero como es verdadera entonces es False"
confirmacion = not comparar_4
print(confirmacion)

"""!= es para comparar si son diferentes, en este caso como son diferentes va imprimir TRUE"""
comparar_si_son_distintos = x != y
print(comparar_si_son_distintos)


"""Ejercicio Booleanos en Python 1
Crea dos variables llamadas   num1   y num2.  Asignale los números de tu elección. Asegurate que el primero sea mayor que el segundo.
Compara   num1y  num2Luego, imprime el valor de la comparación. Asegurate que el resultado sea True."""

num1 = 10
num2 = 5

resultado = num1 > num2
print(resultado)

"""Ejercicio Booleanos en Python 2
Crea tres variables booleanas: condicion1 con valor True, condicion2 con valor False, y condicion3 con valor True.
Escribe un programa que evalúe la siguiente expresión lógica e imprima el resultado.
(condicion1 and condicion3) or condicion2"""

condicion1 = True
condicion2 = False
condicion3 = True

resultado = (condicion1 and condicion3) or condicion2
print(resultado)


"""Ejercicio Booleanos en Python 3
Define tres variables a b y c con valores numéricos de tu elección. 
Escribe un programa que verifique si a es mayor que b y si b es menor que c, imprimiendo True si ambas comparaciones son correctas,
o False en caso contrario. Utiliza operadores de comparación y lógicos en tu respuesta."""

a = 8
b = 5
c = 10

resultado = (a > b) and (b < c)
print(resultado)