x = 3.3
print(x)
y = 1.1 + 2.3
print(y)

print(x == y)  # para la maquina tiene una presión diferente por eso es falso por esto podemos recaer en errores

y_str = format(y, ".2g")  # conversión como string para hacer la suma
print("str =>", y_str)
print(y_str == str(x))

print("***" * 15)

print(y, x)
tolerance = 0.00001
print(abs(x-y) < tolerance)
