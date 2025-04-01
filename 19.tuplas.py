#tuplas son como listas pero que no son modificables 

numbers = (1,2,3,4,5)
string = ("laura", "Emma","Susi","Emma")

print(numbers)
print(type(numbers)) #va decir tuple

print(string)
print(type(string))


print("0 =>", numbers[0])
print("-1 =>", numbers[-1])  #para llamar al ultimo


#CRUD solo la declaración pero no se pueden agregar 

# [].append() #no se puede usar este tipo de herramienta

#numbers.append(10)
#print(numbers)  #Va decir que es un error porque no es posible 

#numbers[1] = "change" #va decir error


print(string)
print(string.index("laura"))
print(string.count("Emma"))