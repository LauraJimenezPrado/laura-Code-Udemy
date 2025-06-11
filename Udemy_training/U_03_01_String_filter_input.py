palabra = "banana"
type(palabra)

dir(palabra)

palabra.count("a")

"""Escribe un programa que tenga dos variables de tipo string palabra y letra.   Almacena una palabra y una letra de tu elección. Utiliza el método adecuado para contar cuántas veces aparece la letra en la variable palabra.

Nota:
• El ejercicio será evaluado por un sistema automático, que considerará la respuesta como incorrecta si hay algún error ortográfico en texto que debes reproducir, o de puntuación, de espacios en blanco adicionales, etc. Por favor, presta mucha atención a esto.
• ¿Recibes un error y no sabes por qué? ¿O tal vez no puedes resolver el ejercicio? Al final de cada sección encontrarás las soluciones a los ejercicios de código del día. Te recomiendo revisarlas antes de colocar preguntas en el área de "Preguntas & Respuestas", 
ya que de esa manera podrás resolver tus dudas mucho más rápidamente que si esperas mi respuesta, que puede demorar hasta 48 horas."""

palabra = "banana"
letra = "a"
cantidad = palabra.count(letra)
print("La Letra", letra , "aparece", cantidad, "veces en la palabra", palabra)

"""Ejercicio Filtrar Strings en Python 2
Escribe un programa en el que declares una variable llamada frase y le asignes el texto que prefieras.
Utiliza el método correspondiente para contar el número de palabras contenidas en ella, asegurándote de que todas estén separadas por un único espacio.
Finalmente, muestra el resultado en pantalla.

Nota:
• El ejercicio será evaluado por un sistema automático, que considerará la respuesta como incorrecta si hay algún error ortográfico en texto que debes reproducir, o de puntuación, de espacios en blanco adicionales, etc. Por favor, presta mucha atención a esto.
• ¿Recibes un error y no sabes por qué? ¿O tal vez no puedes resolver el ejercicio? Al final de cada sección encontrarás las soluciones a los ejercicios de código del día. Te recomiendo revisarlas antes de colocar preguntas en el área de "Preguntas & Respuestas", ya que de esa manera podrás resolver tus dudas mucho más rápidamente que si esperas mi respuesta, que puede demorar hasta 48 horas.
• ¡Muchos éxitos!"""

frase = "Python es un lenguaje muy poderoso"
numero_palabras = len(frase.split())
print("La frase contiene", numero_palabras, "palabras.")


"""Ejercicio Filtrar Strings en Python 3
Escribe un programa en el que declares una variable llamada frase y le asignes el texto que prefieras. Debes cumplir con las siguientes condiciones:

La frase debe contar un espacio al inicio y otro al final, por ejemplo " Python es genial ".
La frase debe tener todas sus palabras separadas por un único espacio.
Crea una variable llamada palabras_en_frase donde  almacenes el número de palabras contenidas en la frase. Utiliza los métodos correspondientes para  conseguir las siguientes acciones en el orden que se describen a continuación:

Eliminar los espacios al incio y al final de la frase.
Contar el número de palabras contenidas en la frase.

Finalmente, muestra el resultado en pantalla."""

frase = " Python es genial "
frase_sin_espacios = frase.strip()
palabras_en_frase = len(frase_sin_espacios.split())
print("La frase contiene", palabras_en_frase, "palabras.")


a = int(input("Dime el primer numero: "))
b = int(input("Dime el segundo numero: "))
suma = a + b
print("La suma es " + str(suma))

"""Ejercicio Input() en Python 1
Escribe un programa en Python que pida al usuario su nombre mediante el uso de la función input.

"Escribe tu nombre: "

El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).
Aclaración:

no deben imprimirse strings adicionales a la respuesta del usuario.
Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas"
Ya que el botón "Ejecutar código" arrojará el siguiente error: EOF when reading a line.

Nota:
• El ejercicio será evaluado por un sistema automático, que considerará la respuesta como incorrecta si hay algún error ortográfico en texto que debes reproducir, o de puntuación, de espacios en blanco adicionales, etc. Por favor, presta mucha atención a esto.
• ¿Recibes un error y no sabes por qué? ¿O tal vez no puedes resolver el ejercicio? Al final de cada sección encontrarás las soluciones a los ejercicios de código del día. Te recomiendo revisarlas antes de colocar preguntas en el área de "Preguntas & Respuestas", 
ya que de esa manera podrás resolver tus dudas mucho más rápidamente que si esperas mi respuesta, que puede demorar hasta 48 horas"""


nombre= input("Escribe tu nombre: ")
print(nombre)

"""Escribir un programa que solicite al usuario su año de nacimiento (almacena esta entrada en una variable llamada nacimiento ), realiza una operación matemática simple con este valor y muestra el resultado. Este ejercicio tiene como objetivo practicar la entrada de datos por parte del usuario, la conversión de tipos de datos y la realización de operaciones matemáticas básicas.
Instrucciones:
Al iniciar el programa, debes pedir al usuario que ingrese el año en que nació utilizando la pregunta: "¿En qué año naciste?" . y almacenar esta entrada en una variable llamada nacimiento
Una vez recibido el año de nacimiento como entrada, debes convertir este valor de una cadena de texto (str) a un número entero (int). Sobre escribe la variable  nacimiento sin crear nuevas variables.
Luego, suma 1 al año de nacimiento convertido y guarda el resultado. Sobre escribe la variable  nacimiento sin crear nuevas variables.
Finalmente, imprime el resultado de esta operación."""

nacimiento = input(" ¿En qué año naciste?")
nacimiento = int(nacimiento)
nacimiento = 1 + nacimiento
print(nacimiento)


"""Desarrolla un programa que le pregunte al usuario la cantidad de kilómetros que desea convertir a millas.
Utiliza la función input() para recoger esta información, conviértela a un valor numérico y realiza la conversión (considera que 1 kilómetro equivale a 0.621371 millas). Finalmente, imprime el resultado.

Instrucciones:
Al iniciar el programa, debes pedir al usuario que ingrese una cantidad de kilómetros utilizando la orden siguiente: 
"Introduce la cantidad de Kilómetros recorridos: "  y almacenar esta entrada en una variable llamada km
Luego, convierte los kilómetros a millas considerando que 1 kilómetro equivale a 0.621371 millas  y guarda el resultado.
Finalmente, imprime el resultado de esta operación.
Aclaración:

no deben imprimirse strings adicionales a la respuesta del usuario.
Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas"
Ya que el botón "Ejecutar código" arrojará el siguiente error: EOF when reading a line.
Nota:
• El ejercicio será evaluado por un sistema automático, que considerará la respuesta como incorrecta si hay algún error ortográfico
en texto que debes reproducir, o de puntuación, de espacios en blanco adicionales, etc. Por favor, presta mucha atención a esto.
• ¿Recibes un error y no sabes por qué? ¿O tal vez no puedes resolver el ejercicio? Al final de cada sección encontrarás 
las soluciones a los ejercicios de código del día. Te recomiendo revisarlas antes de colocar preguntas en el área de 
"Preguntas & Respuestas", ya que de esa manera podrás resolver tus dudas mucho más rápidamente que si esperas mi respuesta, 
que puede demorar hasta 48 horas."""

km = input("Introduce la cantidad de Kilómetros recorridos: ")

km = float(km)

km = km * 0.621371

print(km)

