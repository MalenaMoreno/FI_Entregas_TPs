import re

#Ejercicio 1

# Escribí un programa que verifique si un string tiene AL MENOS un carácter permitido.
# Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]', string))    # . --> al menos un caracter permitido

# def carcateres_permitidos(string):
#     charRe = re. compile('[a-zA-Z0-9]')
#     string = charRe. search(string)
#     return bool(string)
# return bol (charRe.search(string))

print("El string", "ABCDEFabcdef123450", "tiene caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))                      #True

print("El string", "*&%@#!}{", "tiene caracteres permitidos?")
print(caracteres_permitidos("*&%@#!}{"))                                #False

print("El string", "*&%@#!}{123a", "tiene caracteres permitidos?")
print(caracteres_permitidos("*&%@#!}{123a"))                            #True


#Ejercicio 2.
# Escribí un programa que verifique si un string tiene todos sus caracteres, permitidos

def caracteres_permitidos(string):
    return not bool(re.search('[^a-zA-Z0-9]', string))      #con el ^ --> el string NO tiene algo de [esto] 


print("El string", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghuvwxyz0123456789", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghuvwxyz0123456789"))

print("El string", "ABCDEFabcdef123450!", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450!"))      

#not bool --> invierto el valor del booleano
#con el piquito ^ me dice que busque alguno que no este permitido 
#doble negacion


#Ejercicio 3

# Creá un programa que verifique las siguientes condiciones:

# si un string dado tiene una h seguida de NINGUNA O MAS e

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))    #False
print(encontrar_patron("h"))   #Todas True
print(encontrar_patron("he"))
print(encontrar_patron("hee"))
print(encontrar_patron("heeeee"))
print(encontrar_patron("hheeee"))


#Ejercicio 3 .2
# si un string dado tiene una h seguida de UNA O MAS e.

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"

print(encontrar_patron("a"))    #False
print(encontrar_patron("h"))
print(encontrar_patron("he"))   #True
print(encontrar_patron("hee"))


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

# encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"                           # Patron solo letras minusculas 
    if re.search(patron, string) is not None:           # ^afuera, al principio del string
        return "Se encontró el patrón"                  
    else:                                               
        return "No se encontró el patrón"

print(palabras_unidas("aab_bafssh"))
print(palabras_unidas("aAb_bafssh"))
print(palabras_unidas("ab_bAfssh"))


#Ejercicio 5
# Diga si un string EMPIEZA con un número específico

def numero_especifico(numero, string):          
    if re.match(str(numero), string) is not None:       # uso RE.MATCH porque lo busca al princiìo
        return "empieza con el número"
    else:
        return "no empieza con el número"

print(numero_especifico(5, "5sdgf"))
print(numero_especifico(5, "a5sdgf"))
print(numero_especifico(65, "5sdgf"))

#Ejercicio 6

# Dada una lista de strings verifique si se encuentran en una frase dada

lista = ["hola", "tal", "como"]
frase = "hola que tal, como es tu nombre?"

def estan_en(lista, frase):
    for palabra in lista:
        if re.search(palabra, frase) is not None:                           #Uso el SEARCH, que lo encuentre en algún lado 
            print("la palabra '", palabra, "' se encuentra en la frase")
        else:
            print("la palabra '", palabra, "' no se encuentra en la frase") 

estan_en(lista, frase) 


#Ejercicio 7
# string que contenga solamente letras minúsculas, mayúsculas, espacios y números

def solamente(string):
    string = input('Insgrese string: ')
    if re.search('\w\s', string):
        print('este string contiene solo minúsculas, mayúsculas, espacios y números')
    else:
        print('este string NO tiene solo minúsculas, mayúsculas, espacios y números')


#Ejercicio 8 

# Programa que separe y devuelva los caracteres númericos de un string.

string = input('Ingrese string: ')
patron = '\d'

def separe(string): 
    print(re.findall(patron, string))

separe("dashdfhjbsd6fjhbadz84nbs0") 

#Ejercicio 9
# Programa que extraiga los caracteres que estén entre guiones en un string.

def entre_guiones(string):
    return re.findall("-(.*?)-", string)

print(entre_guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))


#Ejercicio 10
# Substrings y las posiciones de estas en una string dado, considerando que las substrings están delimitadas por los caracteres @ o &.

texto = "mi nombre es @ malena y mi apellido & moreno"
palabra_entre = re.findall("@(.*)&",texto)
print(palabra_entre)

for i in palabra_entre:
    print(texto.index(i))


#Ejercicio 11
# Dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def verificar(lista):
    lista_ps = [ ]
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)\w", i):
            lista_ps.append(i)
    return(lista_ps)

print(verificar(lista))

#Ejercicio 12
# Que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|)

text = "mi nombre es: Malena_"

def reemplace(texto):
    return re.sub("[\s_:]", "|", texto)              #re.sub --> reemplaza todas las ocurrencias

print(reemplace(text))

#Ejercicio 13
# Que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

texto = "...Malena ; holaaaa"

def reemplace2(texto):
    return(re.sub('\W', '_', texto, 2))  #el 2 --> que los reemplace 2 veces en este caso, los 2 primeros

print(reemplace2(texto))

#Ejercicio 14
# Programa que reemplace los espacios y tabulaciones por punto y coma.

def hola(string):
    return re.sub("[\t\s]", ";", string)

print(hola("ho?????????hola222222     				"))

#Ejercicio 15
# Validar si una cuenta de mail está escrita correctamente.

def validar_mail(mail):
    return(bool(re.match(r"[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-z]{1,9}\.[a-z]{2,4}(\.[a-z]{2,4})*", mail)))

print(validar_mail("maleemoreno1@gmail.com"))