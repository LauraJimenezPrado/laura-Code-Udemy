# and
print("AND")
# los dos deben ser verdaderos para que sea verdadero
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

'''
And
true and true = true
true and false = false
false and true = false
false and false = false
'''

# las dos condiciones se cumplen por lo tanto es verdadero
print(10 > 5 and 5 < 10)
print(10 < 5 and 5 < 10)  # esta da False

stock = input("ingrese el nuero de stock =>")
stock = int(stock)

# tiene que el inventario mayor a 100 y menor que 1000 puede ser una regla de una interfass
print(stock >= 100 and stock <= 1000)

print("***" * 15)
print("OR")
# si tiene un verdadero va ser verdadero
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

'''
Or (le basta que uno sea true para que la operación sea true)
True or true = true
True or false = true
False or True = true
False or false = false
'''

role = input("Digita el rol =>")
print(role == "admin" or role == "seller")
