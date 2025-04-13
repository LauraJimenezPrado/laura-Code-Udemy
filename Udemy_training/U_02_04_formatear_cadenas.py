color_auto = "rojo"
matricula = 254567

"si quiero imprimir lo siguiente"
print("mi auto es rojo y de matricula 254567")

matricula = str(matricula)

print("mi auto es " + color_auto + "y de matricula " + matricula)

"""pero hay metodos para no hacerlo tan largo"""



"""1 - funcion format"""

print("mi auto es {} y de matricula {}".format(color_auto,matricula))




"""2 - cadenas literales para leerlo mejor, es una actualización de python"""

print(f"Mi auto es {color_auto} y de matricula {matricula}")


