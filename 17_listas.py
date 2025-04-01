#listas de numeros

number = [1,2,3,4,5]
print(number)
print(type(number)) #"List" es tipo de datos

tasks = ["make a dishes", "play videogames"]
print(tasks)

types = [1, True, "hola"]
print(types) 
print(type(types))

print(number[0])

print(tasks[0]) #va aparecer la primera palabra de la lista "make a dishes"

#si quiero remplazar un string NO se puede así de simple:

text = "Hola"
#text[0] = "adios" #va lanzar un error sobre esto

#pero si se pueden remplazar elementos de una lista así:

tasks[0] = "watch platzi courses"
print(tasks) #va imprimir ["watch platzi courses" , "play videogames"] con esta actulización podriamos corregir algo que este mal

#esto lo podemos hacer las veces que queramos

tasks[0] = "do the dishes"
print(tasks)

print(number[:3])

print(True in types) #va buscar si esta el true y lueego va lanzar un true
print("hola" in types) #va buscar el string y si lo encuentra va decir true

