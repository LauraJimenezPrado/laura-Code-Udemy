"""los siguientes no solo sirven para cuando se cumple la condición sino tambien cuando no se cumple"""

"""ELSE que en ingles significa 'si no' . Si no se cumple la condición haz lo siguiente"""

edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Adulto")
else:
    print("Menor")



edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("adolescente")
else:
    print("Menor")


x1, x2, x3 = int(input("Ingresa x1: ")), int(input("Ingresa x2: ")), int(input("Ingresa x3: "))
if x1 > x2:
    if x1 > x3:
        maximo  = x1
elif x2 > x3:
    maximo = x2
else:
    maximo = x3

print(maximo)



"""Ejercicio de Control en Python - IF - ELIF - ELSE 1
Crea un programa donde declares una variable llamada edad, podrás inicializarla con el valor entero de tu preferencia. 
El programa debe imprimir "Tienes {edad} años, eres mayor de edad" si el usuario tiene 18 años o más, y "Tienes {edad} 
años, eres menor de edad" si tiene menos de 18 años."""

edad = 16

if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")
else:
    print(f"Tienes {edad} años, eres menor de edad")


"""Ejercicio de Control en Python - IF - ELIF - ELSE 2
Escribe un programa donde declares una variable llamada calificacion inicializala con un número del 0 al 10. El programa debe imprimir:

"Calificación no válida" para calificaciones mayores a 10.
"Sobresaliente" para calificaciones de 9 o 10.
"Notable" para calificaciones entre 7 y 8.
"Aprobado" para calificaciones de 5 a 6.
"Insuficiente" para calificaciones menores a 5."""

calificacion = 8

if calificacion > 10:
    print("Calificación no válida")
elif calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Notable")
elif calificacion >= 5:
    print("Aprobado")
else:
    print("Insuficiente")


"""Ejercicio de Control en Python - IF - ELIF - ELSE 3
Declara tres variables x1, x2, x3, que contengan tres números enteros distintos. El programa debe imprimir los números en orden ascendente.

El propósito de este ejercicio es fortalecer tu comprensión y habilidad para aplicar estructuras condicionales en Python, 
diseñando una solución que te permita practicar cómo controlar el flujo de un programa basado en condiciones específicas.
Es importante mencionar que, aunque existen métodos más eficientes y directos para ordenar números en Python —tales como las funciones sorted() o el uso de listas—, 
el enfoque de este ejercicio es que desarrolles y apliques la lógica detrás de las estructuras condicionales. Este enfoque te ayudará a mejorar tu pensamiento lógico 
y tu capacidad para resolver problemas de programación de una manera más fundamental."""

x1 = 12
x2 = 7
x3 = 25

if x1 < x2 and x1 < x3:
    if x2 < x3:
        print(x1, x2, x3)
    else:
        print(x1, x3, x2)
elif x2 < x1 and x2 < x3:
    if x1 < x3:
        print(x2, x1, x3)
    else:
        print(x2, x3, x1)
else:
    if x1 < x2:
        print(x3, x1, x2)
    else:
        print(x3, x2, x1)