"""primero crear una agenda vacia"""

agenda = {}
print("AGENDA DE CONTACTOS")
print("___________________")
print("1. Añadir contacto")
print("2. Buscar contacto")
print("3. Editar contacto")
print("4. Eliminar contacto")
print("5. Mostrar contacto")

eleccion = input("Elige una opcion del menú: ")
if eleccion == "1":
    nombre = input("Escribe el nombre del contacto: ")
    telefono = input("Escribe el numero del contacto: ")
    agenda[nombre] = telefono
    print("El contacto fue agregado")
elif eleccion == "2":
    nombre = input("Nombre del contacto ")
    if nombre in agenda:
        print(f"El telefono de {nombre} es {agenda[nombre]}.")
    else:
        print("Ese contacto no existe en la agenda")
elif eleccion == "3":
    nombre = input("Nombre del contacto ")
    if nombre in agenda:
        nuevo_numero = input("Ingrese el nuevo numero: ")
        agenda[nombre] = nuevo_numero
        print(f"El nuevo telefono de {nombre} es {agenda[nombre]}.")
    else:
        print("Ese contacto no existe en la agenda")
elif eleccion == "4":
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        agenda.pop(nombre)
        print("El contacto fue eliminado")
    else:
        print("Ese contacto no existe en la agenda")
elif eleccion == "5":
    print(agenda)
else:   
    print("esa opción es invalida")


