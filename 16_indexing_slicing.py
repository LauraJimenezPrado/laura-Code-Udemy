
#Indexing 
text = "Ella sabe Python"
print(text[0])  #los corchetes cuadrados retoman el caracter buscado el primero es 0
print(text[1])  #busca el caracter numero 1 en este caso la l 
# print(text[999]) # en el caso de que no exista el numero de caracteres va decir error

"""para saber el numero de caracteres existe tenemos "len" pero al contar va numerar de 1 a n+ 
mientras que los caracteres se cuentan desde 0 entonces va ser un error en el codigo """

text = "Ella sabe Python" #son 16 caracteres y len cuenta 16 pero son 15 porque cuenta desde 0 es un error comun

size = len(text)
print("size =>" , size)

print(text[size -1])  #así encuentra el ultimo caracter que es n 
print(text[-1])   #esta es la mejor forma, abreviada para encontrar el ultimo caracter

#Slicing 

print(text[0:5]) #imprime el texto seleccionando exactamente la posición que buscas 
print(text[10:16]) #Pero hay que ser muy preciso para encontrarlo o saberlo
print(text[:10]) #si lo pongo sin decir desde donde, Python asume que es desde cero
print(text[5:-1]) #de un punto hasta el final -1 es el final 
print(text[5:]) #si no se escribe el ultimo python asume que es el ultimo
print(text[:]) #Con este va ir desde el principio hasta el final
print(text[10:16:1]) #estos son saltos de uno en uno P y t h o n
print(text[10:16:2]) #salta de 2 en 2 Pto
print(text[::2]) # va del inicio al final de 2 en 2 El aePto
