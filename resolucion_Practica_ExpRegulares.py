

import re

#Ejercicio 1

"""
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]', string))    # . --> al menos un caracter permitido

# def carcateres_permitidos(string):
#     charRe = re. compile('[a-zA-Z0-9]')
#     string = charRe. search(string)
#     return bool(string)
# return bol (charRe.search(string))

print("El string", "ABCDEFabcdef123450", "tiene caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))

print("El string", "*&%@#!}{", "tiene caracteres permitidos?")
print(caracteres_permitidos("*&%@#!}{"))

"""

#Ejercicio 2.

"""
def caracteres_permitidos(string):
    return not bool(re.search('[a-zA-Z0-9]', string))       #todos los caracteres permitidos 

print("El string", "ABCDEFabcdef123450", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))

print("El string", "ABCDEFabcdef123450!", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450!"))      

"""



#Ejercicio 3

"""
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron,string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))

        #not bool --> invierto el valor del booleano
        #con el piquito ^ me dice que busque alguno que no este permitido 
        #doble negacion

"""

#Ejercicio 3 .2

"""
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))

""" 

# he*  --> una h o una e que puede estar 0 o mas veces 
# [he*] --> una palabra una o mas veces 

#he+ --> una o mas

#Ejercicio 3 .3
"""
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("he"))
print(encontrar_patron("hheeeeey"))

"""

#para ver Q, se utilizan rangos pero en vez de -, utilzo , 


#Ejercicio  4

"""
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"                  #patron solo letras minusculas 
    else:                                               #^afuera, al principio del string
        return "No se encontró el patrón"

print(palabras_unidas("aab_bafssh"))
print(palabras_unidas("aAb_bafssh"))
print(palabras_unidas("ab_bAfssh"))

"""

#Ejercicio 5

def numero_especifico(numero, string):
    if re.match(str(numero), string) is not None:
        return "empieza con el número"
    else:
        return "no empieza con el número"

print(numero_especifico(5, "5sdgf"))
print(numero_especifico(5, "a5sdgf"))
print(numero_especifico(65, "5sdgf"))

#Ejercicio 6