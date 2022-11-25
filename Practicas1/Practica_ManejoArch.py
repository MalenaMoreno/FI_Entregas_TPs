#Manejo de archivos

#Ejercicio 1
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra
# (por ejemplo que imprima cuántas líneas no empiezan con "P")

def starts_with(letra, archivo):
    cuenta = 0 
    with open(archivo, "r") as arch:
        for line in arch:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                cuenta = cuenta + 1
    print("El numero de líneas que no empiezan con", letra , "es", cuenta)

starts_with("h", "prueba_ej1MdA.txt")


#Ejercicio 2 
# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def imprimir_primeras(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[0:numero])

imprimir_primeras(7, "prueba_ej2MdA.txt")


#Ejercicio 3 
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas

def leer_listar_imprimir(numero, archivo):
    with open(archivo, "r") as archi:
        lineas = archi.readlines()
        print(lineas[-1*numero:])

leer_listar_imprimir(7, "prueba_ej3MdA.txt")

#Ejercicio 4 
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def contar_palabras(archivo):
    with open(archivo, "r") as archi:
        archivo = archi.read()
        separa = archivo.split()
        cantidad_palab = len(separa)
        print(cantidad_palab)

contar_palabras("manipulacion_archivos.txt")

#Ejercicio 5 
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea
# y lo guarde en otro archivo.


def ejercicio_5(archivo, letra, archivo2):
    with open(archivo, "r") as archi:
        with open (archivo2, "w") as archi2:
            for line in archivo:
                cambio = line.replace(letra, letra + "\n")
                archi2.write(cambio)

ejercicio_5("bio.txt", "a", "archivo2") #?????


#Ejercicio 6
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def chau_saltos(archivo, archivo_guardar):
    with open (archivo, "r") as ch:
        archivo = ch.read().replace("\n", " ")
    with open (archivo_guardar, "w") as ch2:
        ch2.write(archivo)

chau_saltos("manipulacion_archivos.txt", "prueba.txt")


#Ejercicio 7
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir
# y decir cuantos caracteres tiene.


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
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def docs(doc1, doc2, doc3):
    with open(doc1, 'r') as docu1, open(doc2, 'r') as docu2, open(doc3, 'a') as docu3: 
        docu3.write(docu1.read() + docu2.read())

docs('bio.txt', 'manipulacion_archivos.txt', 'prueba_2.txt')

#Ejercicio 9
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo.
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read()
        lista = palabras.split()
        dic = {}
        for palabra in lista:
            dic[palabra] = int(lista.count(palabra)) / int(len(lista))
        print(dic)

frecuencia("../bio.txt")

#Ejercicio 10

# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1)
# y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

import os, glob

def unir_txt(carpeta1, nombre):
    #carpeta1 es la ruta a esa carpeta
    os.chdir(carpeta1)                                  #me tengo que mover a esa carpeta
    textos = glob.glob("*.txt")
    os.mkdir("Resuelto")                               #Creo una carpeta nueva
    
    with open("Resuelto/"+ nombre, "a") as salida:     #Guardar en esa carpeta toda la inof de los txt
        for archivo in textos:                          #por cada archivo txt 
            with open(archivo, "r") as texto:           #abrilo
                salida.write(texto.read()+ "\n")        

unir_txt("Carpeta1", "salida.txt")          # aca ya se donde estoy parado (ruta relativa)

#con ruta absoluta: hay que indicar carpeta1 con la RUTA

# crear archivo para una carpeta en la q no estoy parado; por eso Resultado/nombre 
# lo estoy abriendo en modo append entonces me lo crea """