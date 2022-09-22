#Ejercicio 1

# Dado el siguiente bloque de código contestar:

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except:
    print("no puedo agregar arroz")

# ¿Es correcto el uso del try...except? ¿Qué cosa/s le modificarías?

# Convendría tener en claro los errores que puedan surgir, en este caso TypeError.
# Dada la lista_super, se le podria agregar...  (TypeError), al bloque de except:

try:
    lista_super + "arroz"
except TypeError:
    print("no puedo agregar arroz")


#Ejercicio 2

# Definir una función que tenga como parámetros una lista de números por un lado y un número por otro
# y devuelva una lista con la división de cada elemento por el número dado.
# Por ejemplo, si le paso ([2,4,6,8], 2), debería retornar [1,2,3,4].
# Tomar las precauciones necesarias.

lista = [2,4,6,8]

def funcion(lista, numero):
    try:
        lista2 = []
        for i in lista:
            lista2.append((i/numero))
        print (lista2)
    except ZeroDivisionError:
        print ("No se puede dividir por cero")
    except:
        print ("Error, no se puede ejecutar la funcion")

funcion([2,4,6,8], 0)


#Ejercicio 3

# Definir un procedimiento, que reciba una lista y un número,
# el cual tiene que agregar el número a la lista, solo si el número es positivo.
# De lo contrario debería generar un error indicando que el número no es positivo.

lista = [2,4,6,8]

def agregar(lista, numero):
    if numero > 0:
        lista.append(numero)
    else:
        raise TypeError("El numero debe ser positivo")

agregar(lista, -1)

print(lista)


