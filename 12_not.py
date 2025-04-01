print(not True)
print(not False)

print("NOT")
# los dos deben ser verdaderos para que sea verdadero
print("not True and True =>", not (True and True)) #resultado false
print("not True and False =>", not (True and False)) #resultado true
print("not False and True =>", not (False and True)) #resultado true
print("not False and False =>", not (False and False)) #resultado true


'''
Not
not true = false
not false = true

'''
stock = input("ingrese el nuero de stock =>")
stock = int(stock)


print(not (stock >= 100 and stock <= 1000)) #si no quiero que acepte un rango de numeros puedo usar esto
