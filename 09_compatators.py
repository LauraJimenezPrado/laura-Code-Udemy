# >
print(7 > 3)
print(3 > 7)
print(7 < 7)  # falso porque no es mayor sino igual

# <
print(5 < 6)
print(6 < 5)
print(5 < 5)

# >=
print(2 >= 1)
print(2 >= 3)
print(2 >= 2)

# <=
print(2 <= 1)
print(2 <= 3)
print(2 <= 2)

# ==
print(6 == 6)
print(5 == 2)

# !=   diferente de
print(6 != 10)
print(6 != 2)
print(6 != 6)

# ahora con strings

print("Apple" == "Apple")
print("Apple" == "apple")  # este es falso porque la a es minuscula

# diferentes tipos de datos
print("1" == 1)  # uno es  str y el otro es int  (al print da False)

age = 27
# puede funcionar como regla para no ingresar datos quq no cumplen con las condiciones como la edad
print(age >= 18)

age = 15
print(age >= 18)  # este va ser Falso
