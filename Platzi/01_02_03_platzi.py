name = "Laura"
last_name = "Jimenez"
print(name)

full_name = name + " " + last_name
print(full_name)

quote = "laura's Name"

print(quote)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1", template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2", template)

template = f"hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)

print("Me llamo \"Bass\"") 

"""el caracter que esta en seguida de un / invertido osea \" ejemplo se va imprimir literalmente, si quiero insertar algo puede ser de esa forma"""

test_tipo_linea = "Esta es una linea \n y esta es otra linea"
print(test_tipo_linea)

"""el \n se podria usar para saltar al siguiente renglon (la n significa nueva linea)"""

print("\testa es  la tercera linea")
"""\t es tabular posea agrega 4 espacios antes de la linea"""


""""si quiero agregar un apostrofe a un codigo por ejemplo una texto en ingles puedo poner \' antes del del apostrofe y se quitara
el error o puedo aclarar que el apostrofe esta afuera y las comillas dobles para encerrar el texto"""

print("Laura's friends")
print('Laura\'s friend')
"""como la barra invertida es una herramienta si quiero imprimirla debo poner dos barras seguidas"""
print("este signo \\ es una barra invertida")

"""Ejercicio:"""
print("A\t"+"B\t"+"C")
print("D\t"+"E\t"+"F")
print("G\t"+"H\t"+"I")

print("Barra Normal: /\nBarra Invertida: \\\n")







