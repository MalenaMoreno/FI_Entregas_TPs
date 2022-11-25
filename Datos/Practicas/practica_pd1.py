import pandas as pd 

# Ejercicio 1
# Escribí un programa que sume, reste, multiplique y divida dos series de números de Pandas.
ser1 = [3, 7, 12, 15, 21]
ser2 = [1, 4, 10, 14, 19]

ds1 = pd.Series(ser1)
ds2 = pd.Series(ser2)

print("Suma: ")
print(ds1 + ds2)

print("\nResta: ")
print(ds1 - ds2)

print("\nMultiplicador: ")
print(ds1 * ds2)

print("\División: ")
print(ds1 / ds2)

# Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales) los elementos de dos series de números de Pandas.

serie1 = [3, 7, 9, 14, 25]
serie2 = [1, 7, 10, 16, 19]

ss1 = pd.Series(serie1)
ss2 = pd.Series(serie2)

print('Igualdad: ')
print(ss1 == ss2)

# Ejercicio 3
# Escribí un programa para convertir un diccionario a una serie de Pandas.

dict = {"a": 10, "b": 20, "c": 30,  "d": 40, "e": 50,}

nueva_serie = pd.Series(dict)

print(nueva_serie)

# Ejercicio 4
# Escribí un programa que dado un diccionario cuyos valores son listas de números, cree otro diccionario con las mismas claves,
# pero donde los valores sean una lista de números donde se potencia un número por el siguiente, tomándolos de a pares.

# Para ser más claros miremos este ejemplo donde si un diccionario es:
dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
# el diccionario resultante debería ser:
# dict2 = {"a": [1, 25], "b": [16, 27]}

# Esto se obtiene al hacer 1 al cubo (el primer par de la lista "a"), y 5 al cuadrado, por un lado; y 4 al cuadrado y 3 al cubo por el otro. 
# Se considera que la cantidad de elementos en las listas siempre es par, por lo que no habría que hacer ninguna comprobación al respecto.
# Se puede usar el dict1 como diccionario de muestra, pero considerá que la lista puede ser más grande.
# Por último hay que convertir este último diccionario en un DataFrame de Pandas.

dict2 = {}

for clave, valor in dict1.items

# Ejercicio 5
# Realizá un programa para crear y mostrar un DataFrame a partir de un diccionario y de unas etiquetas (o labels).

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(datos_ejemplo, index = labels)
print(df)

# Ejercicio 6
# Escribí un programa que muestre un resumen de la información básica de un DataFrame y sus datos.

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(datos_ejemplo, index = labels)
print(df)
print(df.info())

# Ejercicio 7
# Escribí un programa que obtenga las 3 primeras filas de un DataFrame dado.

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(datos_ejemplo, index = labels)

print(df.head(3))

# Ejercicio 8
# Realizá un programa que seleccione e impirma las columnas "nombre" y "puntaje" del DataFrama anterior.

print(df[["nombre", "puntaje"]]) #Entre corchetes un lista, esa lista tiene los nombres de las columnas 

# idem:
# columnas = ["nombre", "puntaje"]
# print(df[columnas]) 

# Ejercicio 9
# Escribí un programa que dado el DataFrame anterior imprima los nombres en mayúscula y la longitud de los mismos en una nueva tabla.

new_dict = {}

for nombre in df["nombre"]:                 #recorro los nombres 
    new_dict[nombre.upper()] = len(nombre)  

df2 = pd.DataFrame(new_dict.items())
print(df2)

