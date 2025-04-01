
if True:
    print("deberia ejecutarse")
if False:
    print("Nunca se ejecuta")

'''
pet = input("¿Cuál es tu mascota favorita?")

if pet == "Perro":
    print("genial tienes buen gusto")

if pet == "Gato":
    print("espero tengas suerte")


stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("el stock es correcto")
else:
    print("El stock es incorrecto")

    


/// Acontinuación el comando elif para que cuando responda la primera pregunta se infiera que las otras respuestas son falsas. 
'''

pet = input("¿Cuál es tu mascota favorita?")

if pet == "Perro":
    print("genial tienes buen gusto")

elif pet == "Gato":
    print("espero tengas suerte")

elif pet == "Pez":
    print("genial y sombrio")

else:
    print("No tienes ninguna mascota interesante")
