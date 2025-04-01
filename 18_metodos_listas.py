
#crud es la posibilidad de crear, leer, cargar y eliminar ( Create, read, update and delete)

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1]= 10 #se agrega 10 a la lista (recordar -1 es la ultima posición)
print(numbers)

#append sirve para agregar un nuevo elemento

numbers.append(15) #por defecto lo agrega al final de la lista
print(numbers)

numbers.insert(0, "hola") #va insertar hola en la posición 0
print(numbers)

numbers.insert(0, 0) #agrega el elemento en la posición y corre los demás 
print(numbers)



numbers.insert(3, "change") 
print(numbers)

tasks=["to do 1", "to do 2", "to do 3"]

#para unir listas:

new_list = numbers + tasks 
print(new_list)

# print(new_list.index("to do 2"))#va decir que el numero de la posición que es 10 

index = new_list.index("to do 2")  
new_list[index] = "to do 99"  #remplaza y nosotros no tenemos que buscarlo
print(new_list)

new_list.remove("change") #para remove hay que saber el nombre exacto
print(new_list)

new_list.pop() # elimina el ultimo elemento de la lista
print(new_list)

new_list.pop(2) #elimina la posición (el 2 es el numero 1, entonces lo elimino)
print(new_list)

new_list.reverse()  #va cambiar el orden antes estaba 1 2 3 ahora va aparecer 3 2 1 
print(new_list)

numbers_2024 = [1, 5 , 2 , 6 , 8]
print(numbers_2024)

numbers_2024.sort() # organiza todos los numeros
print(numbers_2024)

strings =["cd","ab","ef"]
print(strings)

strings.sort()  #organiza por orden de abecedario 
print(strings)

# si yo tratara de usar sort con una tabla como new_list va salir un error porque tiene diferentes tipos de datos mezclados



