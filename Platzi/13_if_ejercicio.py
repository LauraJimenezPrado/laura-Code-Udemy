print("Hola, vamos a indentificar si un numero es par o impar")
Numero = int(input("Introduce un numero: "))
result = Numero % 2
if result == 0:
    print(str(Numero) + " Es un numero par")
else:
    print(str(Numero) + " Es un numero impar")
