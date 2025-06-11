"""estas estan condicionadas a si se cumple una condicion o no, dependiendo de esa verificación, ejecuta una u otra opción"""


temperatura = 22
if temperatura > 20:
    print("hace calor")

"""no va imprimir nada, porque no se cumple la condicion"""
temperatura = 15 
if temperatura > 20:
    print("Hace calor")

temperatura = int(input("Dime la temperatura: "))
if temperatura > 20:
    print("hace calor")

temperatura = int(input("Dime la temperatura: "))
if temperatura > 16 and temperatura < 22:
    print("El clima es agradable")

amigos = ["Juan", "Ana", "Laura"]
nombre =input("Die tu nombre: ")
if nombre in amigos:
    print(f"{nombre} esta en mi grupo de amigos")


temperatura = True
if temperatura:
    print("Hace calor")

if True:
    print("Hace calor")

if 10 > 5 :
    print("Esta linea esta dentro del if")
    print("Esta linea tambien esta dentro del if")
print("esta linea esta fuera del if y se va imprimir siempre")

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

