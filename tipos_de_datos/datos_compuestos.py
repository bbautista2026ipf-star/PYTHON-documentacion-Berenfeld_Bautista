array = ["bautista", "berenfeld", 80, 320.2, True]

# ¿que distingue una lista de una tupla?
# la lista puede modificarse, mientras que la tupla no puede modificarse
tupla = ("bautista", "berenfeld", 80, 320.2, True)


# esto es valido
array[0] = "israel"

# esto no es valido
# tupla[0] = "israel"


print(array[0]) # israel
print(tupla[1]) # berenfeld


# conjuntos
conjunto = {"bautista", "berenfeld", 80, 123.123, True}
print(conjunto)
# Los conjuntos no permiten elementos duplicados, por lo que si agregamos un elemento que no es un duplicado,
# se agregara al conjunto, pero si agregamos un elemento que ya existe en el conjunto, no se agregara y se generara un error.
# es como las tuplas que no pueden modificarse, pero solo sus elementos durante la ejecucion del programa, entonces
# podemos agregar elementos pero mas tarde no podemos agregar ni quitar.
# - No permite repetir elementos
# - No permite acceder a los elementos por su indice
# - No tiene orden, es decir, no se puede garantizar el orden de los elementos

# Diccionarios (dict)
# Los diccionarios son estructuras de datos que permiten almacenar pares de clave-valor.
# Cada clave es unica y se utiliza para acceder a su valor correspondiente. Los diccionarios son mutables, 
# lo que significa que se pueden modificar despues de su creacion. Los diccionarios son utiles cuando se necesitan almacenar datos que se pueden identificar mediante un nombre o una clave unica,
# como por ejemplo, la informacion de un usuario en una aplicacion web.

diccionario = {
    "nombre": "bautista",
    "apellido": "berenfeld",
    "edad": 80,
    "altura": 123.123,
    "activo": True
}
print(diccionario["altura"]) # 123.123