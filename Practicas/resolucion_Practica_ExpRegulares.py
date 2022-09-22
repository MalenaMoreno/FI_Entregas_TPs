import re

#Ejercicio 1


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


#Ejercicio 2.


def caracteres_permitidos(string):
    return not bool(re.search('[a-zA-Z0-9]', string))       #todos los caracteres permitidos 

print("El string", "ABCDEFabcdef123450", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))

print("El string", "ABCDEFabcdef123450!", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450!"))      



#Ejercicio 3


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


#Ejercicio 3 .2

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))

# he*  --> una h o una e que puede estar 0 o mas veces 
# [he*] --> una palabra una o mas veces 

#he+ --> una o mas

#Ejercicio 3 .3

def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("he"))
print(encontrar_patron("hheeeeey"))



#para ver Q, se utilizan rangos pero en vez de -, utilzo , 


#Ejercicio  4

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"                  #patron solo letras minusculas 
    else:                                               #^afuera, al principio del string
        return "No se encontró el patrón"

print(palabras_unidas("aab_bafssh"))
print(palabras_unidas("aAb_bafssh"))
print(palabras_unidas("ab_bAfssh"))


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


lista = ["hola", "tal", "como"]
frase = "hola que tal, como es tu nombre?"

def estan_en(lista, frase):
    for palabra in lista:
        if re.search(palabra, frase) is not None:
            print("la palabra '", palabra, "' se encuentra en la frase")
        else:
            print("la palabra '", palabra, "' no se encuentra en la frase") 

estan_en(lista, frase) 


#Ejercicio 7

def solamente(string):
    string = input('Insgrese string: ')
    if re.search('\w\s', string):
        print('este string contiene solo minúsculas, mayúsculas, espacios y números')
    else:
        print('este string NO tiene solo minúsculas, mayúsculas, espacios y números')



#Ejercicio 8 

string = input('Ingrese string: ')
patron = '\d'
def separe(string): 
    print(re.findall(patron, string))
separe(string) 


#Ejercicio 9

def entre_guiones(string):
    return re.findall("-(.*?)-", string)

print(entre_guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))



#Ejercicio 10

texto = "mi nombre es @ malena y mi apellido & moreno"
palabra_entre = re.findall("@(.*)&",texto)
print(palabra_entre)

for i in palabra_entre:
    print(texto.index(i))


#Ejercicio 11

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def verificar(lista):
    lista_ps = [ ]
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)\w", i):
            lista_ps.append(i)
    return(lista_ps)

print(verificar(lista))

#Ejercicio 12

text = "mi nombre es: Malena_"

def reemplace(texto):
    return re.sub("[\s_:]", "|", texto)              #re.sub --> reemplaza todas las ocurrencias

print(reemplace(text))

#Ejercicio 13

texto = "...Malena ; holaaaa"

def reemplace2(texto):
    return(re.sub('\W', '_', texto, 2))  #el 2 --> que los reemplace 2 veces en este caso, los 2 primeros

print(reemplace2(texto))

#Ejercicio 14

def hola(string):
    return re.sub("[\t\s]", ";", string)

print(hola("ho?????????hola222222     				"))


#Ejercicio 15

def validar(mail):
    patron = " "
    return bool(patron, mail)

print

