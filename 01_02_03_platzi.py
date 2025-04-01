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
