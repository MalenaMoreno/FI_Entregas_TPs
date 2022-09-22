#De Intro_a_Python --> https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/intro_python_tutorial.md

# DESAFÍO 1: ¿Qué pasos nos faltaron? ¿Podes pensar otras posibles situaciones que no estemos contemplando
# (como por ejemplo que no haya yerba en el yerbero)?
# Agregá a la guía para preparar mate(script) los pasos, problemas posibles y
# las soluciones que se te ocurran en sentencias u ordenes sencillas
# (ejemplo; verificar si hay yerba en el yerbero. Si no hay agregar, si hay llenar el mate)

"""

Paso 1) Seleccionar el mate
Paso 2) Buscar el yerbero
Paso 3) Verificar si el mate está vacío:
    Momento decisivo:
        Paso 4) Si el mate está vacío, llenarlo con la yerba del yerbero.
        Paso 5) Si el mate está lleno:
                Paso 7) Vaciarlo en una maceta
                Paso 8) Llenarlo con la yerba del yerbero.


mate = mate seleccionado
yerbero = lata de yerba
maceta = maceta con cactus del balcón 

    if mate está vacio:
        llenar mate con yerba del yerbero
    de lo contrario:
        vaciar mate en maceta
        llenar mate con yerba del yerbero

"""

# DESAFÍO II: Abrí la terminal de Python que tengas instalada en tu computadora
# y luego abrí Visual Code y luego presioná las teclas Ctrl + J.
# Se abrirá una terminal en el editor de código.
# ¿Cómo es el prompt en cada caso?
# ¿Qué lenguaje "entiende" la terminal de Visual Code?

#Calculadora...

"""
print(3*5) #multiplica
print(8/4) #divide

""" 

"""
edad_lola = 13
edad_ana = 32
edad_lola == edad_ana
# Para pensar 🤔:¿Cuál es el resultado? ¿Qué tipo de dato es? Falso, es un booleano

afirmacion = "si"
gran_afirmacion = "SI"
gran_afirmacion == afirmacion
# Para pensar 🤔:¿Qué resultado nos da? Falso ¿Por qué? Mayusculas != minusculas

# Para pensar 🤔:¿Posición tendrá la letra "C' en el string "Marie Curie"? ¿Por qué?
# Posicion 6. La "cuenta" en string o cadenas arranca en 0 

saludo = "Hola mundo"
saludo[0:3]
# Para pensar 🤔:¿Qué resultado nos dá el código anterior? ¿Por qué?
    #  devuelve "Hol" 
    #   saludo[0:3] --> incluye caracteres 0,1 y 2 (no incluye al 3, sí al 0)
# ¿Qué pasa si removemos el último número
    # saludo[0:] --> devuelve todo el string, desde la posicion 0 hasta el final 

"""

saludo = "Hola mundo"
len(saludo) #cantidad de caracteres
saludo.upper() #todo a mayus
saludo.lower() #todo a minusculas
saludo.count('o') #cuenta caracteres == "o"
saludo.replace('o','a') #remplaza o por a

# Desafío III: Probá las lineas anteriores y
# anotate para qué sirve cada uno de los métodos y funciones.

# Para pensar 🤔: ¿Se podrán combinar los métodos? SI
    # Probá hacer saludo.upper().lower() ¿Qué dá? ¿Por qué?

# Desafío IV: Vimos que el método replace nos permite reemplazar un caracter 
# por otro de un string dado, pero nos dejará reemplazar un segemento más largo?
# Probá hacer saludo.replace("mundo", "terricolas")

# Para pensar 🤔: ¿Si imprimís saludo luego de ejecutar la linea anterior qué obtenés? 
# ¿Cambió el valor de la variable? NO

lista = [2,5,4]
lista[0] # --> devuelve 2 

len(lista) # --> longitud de lista, cantidad de elementos 

lista.append('25') # --> agrega a la lista,  
lista.remove('25') # --> saca de  la lista,  

lista.index("string") # --> posicion de tal string en la lista

# Para pensar 🤔: ¿Cómo harías para obtener todos los valores de un diccionario?

## Desafío VI:  Suponiendo que cada cebada de mate consume del 30 ml de agua.
# Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos 
# consumiremos para un ronda dada (es decir una cantidad de personas dada).

def termos_por_ronda(personas): 
    return (personas * 30) / 1000

# Desafío VII: Siempre con los mates, vienen bien unas facturitas 🥐🥐
# ¿Si hacemos una vaquita ? Vaquita se le dice en Argentina a hacer una colecta de plata
# para un fin común. Creá función que nos permita dividir los costos de una docena de
# facturas entre cierta cantidad de comensales.

def vaquita(costos, comensales):
    return costos / comensales

## Desafío VIII: En una ronda pequña de mate 🧉 no hace falta llenar tooooodo el termo, con un poco de agua quizás alcanza.
# Definí una función calcular_cantidad_de_agua que espere una cantidad de personas como argumento
# y devuelva la cantidad de mililitros con los que tenemos que cargar el termo.

# 👀 ¡OJO! Si llega a 1000 debería retornar la advertencia "vas a necesitar más de un térmo"

def calcular_agua(personas): 
    if termo >= (personas * 30): 
        return personas * 30
    else:
        return "se necesita mas de un termo"


pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
pedido["Ana"]
# extraer la lista de comensales que se suman al pedido haciendo:

pedido.keys()

# recorrer esa lista para acceder en cada caso al gusto que eligió cada persona:
# Obtenemos la lista de comensales

lista_comensales = pedido.keys()

def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])

# Para pensar 🤔: ¿Qué nos imprime el procedimiento de anterior? ¿Qué significa i?

# nos faltaría sumar +1 a la lista veggies si el valor es "veganas" o sumar +1 a la lista no_veggies
# si el valor se corresponde con "no veggie"... ¡Pero eso te toca vos!

## Desafío IX: Modificá la función empanadas_por_gusto() para que devuelva la cantidad de empenadas
# de cada gusto que deben pedirse a la casa de comidas

gustos = {"no_veggie": 0, "veggie": 0} 
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
lista_comensales = ["Ana", "Paul", "Luz"]
def empanadas_por_gusto(): 
    for comensal in lista_comensales: 
        gustos[pedido[comensal]] += 1

print(gustos)
"""
"""

