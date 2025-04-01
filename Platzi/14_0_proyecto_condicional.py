print("Hola, bienvenido al Juego PIEDRA PAPEL O TIJERA")


user_option = input("Piedra papel o tijera => ")
user_option = user_option.lower()
computer_option = "papel"

if user_option == computer_option:
    print("Empate")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("piedra gana a tijera")
        print("User gano")
    else:
        print("papel gana a piedra")
        print("Computer gano")
elif user_option == "papel":
    if computer_option == "piedra":
        print("papel gana a piedra")
        print("user gano")
    else:
        print("tijera gana a papel")
        print("Computer gano")
elif user_option == "tijera":
    if computer_option == "papel":
        print("tijera gana a papel")
        print("user gano")
    else:
        print("piedra gana a tijera")
        print("Computer gano")
