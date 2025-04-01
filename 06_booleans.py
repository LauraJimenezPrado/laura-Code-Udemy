is_single = True
print(is_single)

is_single = False
print(is_single)

print(not True)
print(not False)

is_single = not is_single
print(is_single)


name = "Laura"
print(type(name))
name = 27
print(type(name))
name = True
print(type(name))

print("Nicolas" + "Molina")
print(10 + 20)
print("Nicolas" + "12")

age = 27
print("Mi edad es " + str(age))

print(f"Mi edad es {age}")


age = input("¿Cual es tu edad actual ->")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años sera {age}")


name = 'Juana'
print(name)
age = '10'
print(age)
total = int(age) + 10

template = f"Hola mi nombre es {name}, tengo {
    age} años y en 10 años tendré {total} años"
print(template)
