"""estas estan condicionadas a si se cumple una condicion o no, dependiendo de esa verificación, ejecuta una u otra opción"""


temperatura = 22
if temperatura > 20:
    print("hace calor")

"""no va imprimir nada, porque no se cumple la condicion"""
temperatura = 15 
if temperatura > 20:
    print("Hace calor")

"""si el usuario escribe un numero menor no va imprimir algo, solo si es un numero mayor"""
temperatura = int(input("Dime la temperatura: "))
if temperatura > 20:
    print("hace calor")


"""se deben cumplir las dos para que imprima algo"""
temperatura = int(input("Dime la temperatura: "))
if temperatura > 16 and temperatura < 22:
    print("El clima es agradable")


"""tambien lo podemos usar para saber si algo esta incluido en una colección"""
amigos = ["Juan", "Ana", "Laura"]
nombre =input("Dime tu nombre: ")
if nombre in amigos:
    print(f"{nombre} esta en mi grupo de amigos")

"""va imprimir hace calor porque se le asigno que el valor es verdero """
temperatura = True
if temperatura:
    print("Hace calor")

"""esto no tiene sentido, pero siempre que se le asigna true va imprimirlo"""
if True:
    print("Hace calor")



"""es importante conservar la jerarquia de las lineas, para que python sepa que esta dentro del if"""
"""se van a imprimir las 3, las dos primeras porque se cumple el ir y la otra porque esta afuera y siempre se va imprimir"""
if 10 > 5 :
    print("Esta linea esta dentro del if")
    print("Esta linea tambien esta dentro del if")
print("esta linea esta fuera del if y se va imprimir siempre")


"""ahora, las dos primeras no se van a imprimir porque no se cumple la regla, pero si se va imprimir la que esta afuera"""
if 10 > 20 :
    print("Esta linea esta dentro del if")
    print("Esta linea tambien esta dentro del if")
print("esta linea esta fuera del if y se va imprimir siempre")



"""Ejercicio de Control en Python - IF 1
Escribe un programa que defina una variable edad con un valor entero de tu preferencia. Utiliza una estructura de control if para imprimir la siguiente cadena literal:
Tienes {edad} años. Eres mayor de edad
Si edad es mayor  a 18."""


edad = 20

if edad > 18:
    print(f"Tienes {edad} años. Eres mayor de edad")


"""Ejercicio de Control en Python - IF 2
Desarrolla un programa que defina dos variables, usuario  y  contraseña. Luego, escribe una estructura de control que verifique si el usuario es igual a "admin" y si la contraseña es igual a "abc123". Si ambas condiciones se cumplen, imprime "Acceso concedido"

Utiliza el operador matemático de doble igualdad (==) para preguntar con un IF si se cumple determinada condición. Por ejempo: if usuario == "admin"""

usuario = "admin"
contraseña = "abc123"

if usuario == "admin" and contraseña == "abc123":
    print("Acceso concedido")



"""Ejercicio de Control en Python - IF 3
Dada una lista de amigos amigos = ["Juan", "Ana", "Laura"], escribe un programa donde definas una variable llamada nombre y coloques un nombre de tu elección. Si el nombre está en la lista amigos, el programa debe imprimir "{nombre} está en mi grupo de amigos", 
reemplazando  con el nombre ingresado por el usuario. Si el nombre no está en la lista, el programa no debe imprimir nada."""

amigos = ["Juan", "Ana", "Laura"]
nombre = "Ana"

if nombre in amigos:
    print(f"{nombre} está en mi grupo de amigos")

