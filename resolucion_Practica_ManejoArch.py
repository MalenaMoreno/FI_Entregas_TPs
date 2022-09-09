#manejo de archivos

#Ejercicio 1

"""
def starts_with(letra, archivo):
    cuenta = 0 
    with open(archivo, "r") as arch:
        for line in arch:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                cuenta = cuenta + 1
    print("El numero de líneas que no empiezan con", letra , "es", cuenta)

starts_with("h", "prueba_ej1MdA.txt")

"""

#Ejercicio 2 

"""

def imprimir_primeras(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[0:numero])

imprimir_primeras(7, "prueba_ej2MdA.txt")

"""

#Ejercicio 3 

"""

def leer_listar_imprimir(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[-1*numero:])

leer_listar_imprimir(7, "prueba_ej3MdA.txt")

"""
#Ejercicio 4 

def contar_palabras(archivo):
    with open(archivo, "r") as archi:
        

#Ejercicio 10
# Escribí un programa que lea todos los archivos.txt de una carpeta dada (Carpeta1)
# y los añada a un archivo dentro de la carpeta Resultado,
# que a su vez se tiene que encontrar dentro de Carpeta1.

import os, glob

"""

def unir_txt(carpeta1, nombre):
    #carpeta1 es la ruta a esa carpeta
    os.chdir(carpeta1)                                  #me tengo que mover a esa carpeta
    textos = glob.glob("*.txt")
    os.mkdir("Resultado")                               #Creo la carpeta
    with open("Resultado/"+ nombre, "a") as salida:
        for archivo in textos:                          #por cada archivo txt 
            with open(archivo, "r") as texto:           #abrilo
                salida.write(texto.read()+ "\n")        #???

unir_txt("Carpeta1", "salida.txt") 

"""

