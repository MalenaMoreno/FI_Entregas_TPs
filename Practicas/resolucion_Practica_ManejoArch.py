#manejo de archivos

#Ejercicio 1

def starts_with(letra, archivo):
    cuenta = 0 
    with open(archivo, "r") as arch:
        for line in arch:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                cuenta = cuenta + 1
    print("El numero de líneas que no empiezan con", letra , "es", cuenta)

starts_with("h", "prueba_ej1MdA.txt")


#Ejercicio 2 


def imprimir_primeras(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[0:numero])

imprimir_primeras(7, "prueba_ej2MdA.txt")


#Ejercicio 3 


def leer_listar_imprimir(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[-1*numero:])

leer_listar_imprimir(7, "prueba_ej3MdA.txt")

#Ejercicio 4 

def contar_palabras(archivo):
    with open(archivo, "r") as archi:
        archivo = archi.read()
        separa = archivo.split()
        cantidad_palab = len(separa)
        print(cantidad_palab)

contar_palabras("manipulacion_archivos.txt")

#Ejercicio 5 

def ejercicio_5(archivo, letra, archivo2):
    with open(archivo, "r") as archi:
        with open (archivo2, "w") as archi2:
            for line in archivo:
                cambio = line.replace(letra, letra + "\n")
                archi2.write(cambio)

ejercicio_5("bio.txt", "a", "archivo2") #?????


#Ejercicio 6

def chau_saltos(archivo, archivo_guardar):
    with open (archivo, "r") as ch:
        archivo = ch.read().replace("\n", " ")
    with open (archivo_guardar, "w") as ch2:
        ch2.write(archivo)

chau_saltos("manipulacion_archivos.txt", "prueba.txt")


#Ejercicio 7

def palabra_mas_larga(archivo):
    with open(archivo, "r") as arch:
        largo = 0
        palabra_larga = ""
        variab = arch.read().split()
        
        for palabra in variab:
            if len(palabra) > largo:
                largo = len(palabra)
                palabra_larga = palabra
        print("La palabra mas larga es ", palabra_larga, " y su largo es: ", largo)

palabra_mas_larga("manipulacion_archivos.txt")


#Ejercicio 8

def docs(doc1, doc2, doc3):
    with open(doc1, 'r') as docu1, open(doc2, 'r') as docu2, open(doc3, 'a') as docu3: 
        docu3.write(docu1.read() + docu2.read())

docs('bio.txt', 'manipulacion_archivos.txt', 'prueba_2.txt')

#Ejercicio 9


#Ejercicio 10

import os, glob

def unir_txt(carpeta1, nombre):
    #carpeta1 es la ruta a esa carpeta
    os.chdir(carpeta1)                                  #me tengo que mover a esa carpeta
    textos = glob.glob("*.txt")
    os.mkdir("Resultado")                               #Creo la carpeta
    with open("Resultado/"+ nombre, "a") as salida:
        for archivo in textos:                          #por cada archivo txt 
            with open(archivo, "r") as texto:           #abrilo
                salida.write(texto.read()+ "\n")        

unir_txt("Carpeta1", "salida.txt") 


