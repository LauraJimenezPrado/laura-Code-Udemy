
fecha= "29-05-2025"
saludo="Hello"
tipo_de_cambio = 0.88

saludo_complemento = "\n\nI am glad to help you today"

Nombre= input("\nPlease introduce your name: ")
ID= input("\nCould you please introduce your ID: ")

wellcome = saludo + " " + Nombre + saludo_complemento + "\nDate: " + fecha + "\nPlease, remember this transaction is a exchange to EUROS"

print(wellcome)

dolares = input("Please introduce the quantity is DOLLARS: ")
dolares_float =float(dolares)
confirmacion = "OK, I am going to exchange your " + str(dolares_float) + "DOLARS  \n and the exchange rate today is " + str(tipo_de_cambio)
print(confirmacion)

euros_a_recibir = float(dolares_float *tipo_de_cambio)
print("you will receive " + str(euros_a_recibir) + "EUROS")


billetes_10 = euros_a_recibir //10
billetes_1=(euros_a_recibir - (billetes_10*10))//1
coins= euros_a_recibir % 1

print("")
print("quantity of dolars that I received:")
print(dolares)
print("Euros that you will receive")
print(euros_a_recibir)
print("")
print("you will receive the quantity of euros by the following form")
print("10 dollar bills: ")
print(billetes_10)
print("")
print("1 dollar bills: ")
print(billetes_1)
print("")
print("Coins: ")
print(coins)
print("")
print("Thank you for using our services " + Nombre)
