Nombre = "Bautista"

print(Nombre)


numero = 100
numero += 10
numero -= 100

print(numero)

bienvenida = "Hola " + Nombre + " ¿como estas?"
print(bienvenida)



# la funcion de format (f) nos permite concatenar variables dentro de un string de manera mas facil y rapida, es el 
# equivalente a concatenar con el simbolo $ en javascript: 
# bienvenida2 = "hola ${nombre} ¿como estas?"

bienvenida2 = f"Hola {Nombre} ¿Como estas?"
print(bienvenida2)


# Operadores de pertenencia: in y not in
print("Hola" in bienvenida2) # True
print ("Hola" not in bienvenida2) # False


# En js solemos usar el camelcase para nombrar variables, en python se suele usar el snakecase
# EN JS
camelCase = "Javascript"

# EN PYTHON
snake_case = "Python"