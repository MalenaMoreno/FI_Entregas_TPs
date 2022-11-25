
# PARTE 1

#ejercicio 1 

string = input("ingrese string: ")
print(len(string))

#ejercicio 2

a = "Fundamentos"
print(a[4:6].upper())

#ejercicio 3

nombre = input("nombre y apellido:")
print ("hola " + nombre)

#ejercicio 3

nombre = input("nombre: ")
apellido = input("apellido: ")
print("hola", nombre, apellido)

#ejercicio 4

n = input("nombre ")
a1 = input("apellido: ")
a2 = input("apellido: ")
print(n.capitalize() , a1.capitalize(), a2.capitalize())

#ejercicio 5

num1 = int(input("numero1: "))
num2 = int(input("numero2: "))
num3 = int(input("numero3: "))
print ((num1 + num2 + num3) /3)

#ejercicio 6

tiempo = int(input("Ingrese cantidad de minutos: "))
horas = tiempo // 60
minutos = tiempo % 60 

print (horas," horas y", minutos, " minutos")

# ejercicio 7

sueldo_base = int(input("ingrese sueldo: "))

extra_por_ventas = int(sueldo_base * (10/100) * 4)
print(extra_por_ventas)

total = (extra_por_ventas + sueldo_base)
print(total)

#ejercicio 8

correctas = int(input("cantidad de respuestas correctas: "))
incorrectas = int(input("cantidad de respuestas incorrectas: "))
en_blanco = int(input("cantidad de respuestas en blanco: "))

nota_final = (correctas * 4) - incorrectas 
print(nota_final)


## ejercicio en grupo  

sueldo_anual = int(input("Cual es su sueldo anual: "))
costo_total = int(input("Cual es costo de la casa: "))
porcentaje_ahorrado = int(input("Dinero a ahorrar por mes: "))/100

porcentaje_deposito = costo_total * 0.25

cantidad_ahorrada = 0

g = 0.04 
g_por_mes = g/12


# PARTE 2 

# ejercicio 1

cadena = input("ingrese cadena: ")

if cadena[0] == cadena.capitalize()[0]:
     print("Mayuscula")
else:
     print("Minuscula")


# ejercicio 2 

num = int(input("Ingrese un numero: "))

if num > 0:
     print("Positivo")

if num < 0:
     print("Negativo")

if num % 2 == 0 or num == 0:
     print("Par")

else:
     print("Impar")


# ejercicio 3

num_dado = int(input("ingrese numero: "))

if num_dado >= 1 and num_dado <= 6:
    print(abs(num_dado - 7))
else:
    print("el numero ingresado es incorrecto")


# ejercicio 4

zona = input(("ingrese direccion: "))
peso = int(input("ingrese peso en kg: "))

if peso <= 5:
    if zona == "America Central":
        costo = (peso*1000) * 15.00
    elif zona == "America del Sur":
        costo = (peso*1000) * 10.00
    elif zona == "Europa":
        costo = (peso*1000) * 24.00
    elif zona == "Asia":
        costo = (peso*1000) * 30.00
    elif zona == "America del Norte":
        costo = (peso*1000) * 18.00
    print("El costo es de " + str(abs(costo)))
else:
    print("No se puede transportar")


# ejercicio 5

dia = int(input("ingrese numero: "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miercoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sabado")
    elif dia == 7:
        print("Domingo")
else:
    print("el numero ingresado es incorrecto")


# LISTAS

# ejercicio 6

lista = [ input("ingrese elemento 1: "), input("ingrese elemento 2: "), input("ingrese elemento 3: "), input("ingrese elemento 4: "),
 input("ingrese elemento 5: ") ]

print(lista)

lista2 = list.reverse(lista)

print(lista2)

# ejercicio 7

numero = int(input("ingrese numero: "))
lista = [ ]

while numero >= 0 
    lista.append(numero)

print(lista)

# ejercicio 8

l1 = [1,2,3,4,5]
l2 = [5,2,3,9,8]
l3 = [6,4,6,13,13]

for elemento in l1:
    print(elemento)

for indice in range(5):
    print(l2[indice])
    print(l1[indice])

# ejercicio 9

l_nombre = []
l_edad = []

nombre = input("ingrese nombre: ")
edad = input("ingrese edad: ")

while nombre != "*":
    l_nombre.append(nombre)
    l_edad.append(edad)
    nombre = input("ingrese nombre: ")       #sigue agregando alumnos 
    if nombre == "*":
    print("la edad máxima de los alumnos es: " + max(l_edad))


# DICCIONARIOS 

# ejercicio 10

dic = {} 
cadena = input("inserte adena de caracteres: ") 
for caracter in cadena: 
  dic[caracter] += 1
else: 
  dic[caracter] = 1

for clave, valor in dic.items(): 
  print(clave, valor)

# ejercicio 11

dic = {} 
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper(): 
  dic[letra] = 0

cadena = input("Ingrese cadena de caracteres: ")

for caracter in cadena: 
  if caracter.lower() in alfabeto: 
    dic[caracter] += 1
for campo, valor in dic.items(): 
  print (campo, valor)


# ejercicio 12

cantidad = int(input("ingrese cantidad de alumnos: "))
alumnos = {} 

for numero in range(cantidad): 
  alumno = input("ingrese nombre del alumno: ")
  notas = [] 
  nota = int(input("nota: "))
  while nota >= 0:
    notas.append(nota)
    nota = int(input("nota: "))
  alumnos[alumno] = notas 

for alumno in alumnos: 
  print(alumno, sum(alumnos[alumno]) / len(alumnos[alumno])) 


# FUNCIONES

# ejercicio 13

def esMultiplo(numero1, numero2):
    if (numero2 % numero1 == 0) or (numero1 % numero2 == 0):
        print(str(numero2) +" es multiplo de " + str(numero1))
    else:
        print(False)

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

esMultiplo(num1, num2)

# ejercicio 14

def temperatura_media(t_max, t_min):
    print( (t_max + t_min ) / 2)


dias = int(input("cuantos dias?: "))

for dia in range(dias):

    tmax_dia = int(input("ingrese temperatura maxima: "))
    tmin_dia = int(input("ingrese temperatura minima: "))

    temperatura_media(tmax_dia, tmin_dia)

# ejercicio 15
#falta terminar

socios = [{ "numero": 1 , "nombre y apellido": "Florencia Ocampo", "fecha_ingreso": "14/09/2001", "cuota": "Si"},
{ "numero": 2 , "nombre y apellido": "David Estévez", "fecha_ingreso": "14/09/2001", "cuota": "Si"},
{ "numero": 3 , "nombre y apellido": "Sofía Cáceres", "fecha_ingreso": "14/09/2001", "cuota": "Si"}]


def cantidad_de_socios(lista):
    cantidad = 0
    for dic in lista:
        cantidad = cantidad + 1 
    print(cantidad)

n = input("numero de socio: ")

def registrar(socio_num):

    print(socios["numero"])




