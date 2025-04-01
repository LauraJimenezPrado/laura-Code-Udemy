'''
user_answer = input(
    "Hola, conoces a Laura? Sabes que lenguaje de programación conoce:")

if "python" in user_answer:
    print("Entonces probablemente puede ayudarme con mi ejercicio de analisis de datos")
else:
    print("Quiero encontrar a alguien que sepa Python")

text = "Laura sabe programar en Python"
print("JavaScript" in text)
print("Python" in text)

if "Python" in text:
    print("Entonces probablemente puede ayudarme con mi ejercicio de analisis de datos")
else:
    print("Yo no se usar JavaSript")

# los espacios en los caracteres tambien cuentan
size = len("amor") #len cuenta el numero de caracteres
print(size)
'''

text = ("Él sabe programar en Python")
print(text)
print(text.upper())  # lo convierte en mayusculas
print(text.lower())  # lower() lo convierte a minusculas
# count() cuenta numero de letras o caracteres buscados en este caso la "a"
print(text.count("a"))

# convierte en contrarios, mayusculas a minusculas y minusculas a mayusculas
print(text.swapcase())  #pasa las mayusculas a minusculas y las mayusculas a minusculas
print(text.startswith("Él"))  # si inicia con "" va decir true
print(text.endswith("Java"))  # si termina con "" va decir true
print(text.replace("Python", "Java"))  # remplazar una palabra por otra

text_2 = "este es un titulo"
print(text_2) 
print(text_2.capitalize())  # pone mayuscula la primera letra
print(text_2.title())  # pone mayuscula la primera de cada palabra
print(text_2.isdigit())  # revisa si es un digito
# sabemos que es un string pero puede detectar si puede ser un digito
print("938".isdigit())  # si es un digito va decir true. si es un string pero es un numero a la vista puede detectar si es un potencial digito

