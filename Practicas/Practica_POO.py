# Ejercicio 1

    # Dada la siguiente clase, identificá la interfaz
    # y el estado de la misma:

from curses import KEY_MARK

class Perro: 
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

# Perro nombre de la clase
# Interfaz: cojunto de mensajes, de métodos que entiende
# Estado de una clase: conjunto de atributos 

# Ejercicio 2

    # Modificá el método volar de la clase Golondrina visto en la clase de teoría
    # de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (10 + kms < self.energia):
        self.energia -= 10 + kms       #la energia tiene que se
    else:
        print ("No puedo volar esa distancia, no tengo suficiente energia")

# Ejercicio 3

    # Creá una clase Notebook cuyo estado sea: marca, modelo y precio,

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio 

    #  y que tenga un método que le aplique un descuento al precio,
    #  el cual tiene que recibir un número entero (el porcentaje de descuento)
    #  y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento.

    def descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * (porcentaje/100))

    def precio_actual(self):
        return self.precio

#  Por último hay que instanciar esta clase y en algunos casos aplicar este descuento

notebook1 = Notebook("Asus", "R5362l", 80000) 
notebook1.descuento(50)
print(notebook1.precio_actual())

# Ejercicio 4

# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno
# el valor que se ingresa, recordando el valor actual.
# También puede resetear este valor y al hacerlo se pone en cero.
# Además es posible indicar directamente un número nuevo que reemplace al valor actual.

# Este objeto debe entender los siguientes mensajes:
# inc()
# dis()
# reset()
# valorActual()
# valorNuevo(nuevoValor)

# Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

class Contador: 

    def __init__(self, valor):
        self.valor = valor

    def inc(self):
        self.valor +=1

    def dis(self):
        self.valor -= 1

    def reset(self):
        self.valor = 0 

    def valor_actual(self):
        print(self.valor) 

    def nuevo_valor(self, nuevoValor):
        self.valor = nuevoValor  

# Ejercicio 5

# Modificá lo anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje.
# Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización"
# (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando,
# y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador: 
    def __init__(self, valor): 
        self.valor = valor
        self.comando = ''

    def dis(self): 
        self.valor -= 1
        self.comando = 'disminuye'

    def inc(self): 
        self.valor += 1
        self.comando = 'incrementa'

    def reset(self): 
        self.valor = 0 
        self.comando = 'reset'
    
    def valor_actual(self):
        return self.valor

    def nuevo_valor(self, valor): 
        self.valor = valor 
        self.comando = 'actualiza'

    def ultimo_comando(self): 
        print(self.comando)

# Ejercicio 6

# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar.
# Este objeto debe entender los siguientes mensajes:

# cargar(numero)
# sumar(numero)
# restar(numero)
# multiplicar(numero)
# valorActual()

class Calculadora:
    def __init__(self):     
        self.valor = None

    def cargar(self, valor):       #SETTER: asignarle un valor al atributo
        self.valor = valor

    def sumar(self, suma): 
        self.valor += suma

    def multiplicar(self, multiplicador): 
        self.valor *= multiplicador 

    def restar(self, resta): 
        self.valor -= resta
    
    def valorActual(self):      #GETTER: devuelve el valor de un atributo, no asigna nada
        print(self.valor)

#Cuantos getters podrias tener por clase? La cantidad de taributos que tenga, cada atributo tinee un getter  
#Getter metodo que devuelve el valor de un atributo en particular
#Setters modifica o asigna un valor a ese atributo


# Ejercicio 7
  
class Gorriones:

    def __init__(self):         #no hay atributos en parametros
        self.gramosActuales = 0
        self.kmsActuales = 0 
        self.listaGramos = []
        self.listaKms = []

    def comer(self,gramos):
        self.listaGramos.append(gramos)
        self.gramosActuales += gramos

    def volar(self, kms):
        self.vuelos.append(kms)
        self.kms += kms
     
    def CSS(self):
        if self.gramosActuales > 0:
            return self.kmsActuales / self.gramosActuales
        else:
            None
    
    def cssp(self):
        if self.gramosActuales > 0:
            return max(self.kmsActuales) / max(self.gramos.Actuales)
        else:
            None
    
    def CSSV(self):
        if self.gramosActuales > 0:
            return len(self.vuelos)/len(self.comidas)
        else:
            None
    
    def esta_en_equilibrio(self):
        return self.CSS() > 0.5 and self.CSS < 2

# PARTE 2

# Ejercicio 2

# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio.
# Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_en_equilibrio(self):
    if self.energia >= 150 and self.energia <= 300:
        return ("esta en equilibrio")

#Ejercicio 3

class Ornitologo:

    def __init__(self):
        self.aves = []

    def estudiar_ave(self, ave):
        self.aves.append()

    def aves_en_estudio(self): 
        return self.aves()

    def aves_en_equilibrio(self):
        return [ self.aves[i].esta_en_equilibrio() for i in range(len(self.aves)) ]

    def realizar_rutina_sobre_aves(self):
        [ self.aves[i].comer(80) for i in range(len(self.aves)) ]
        [ self.aves[i].volar(70) for i in range(len(self.aves)) ]
        [ self.aves[i].comer(10) for i in range(len(self.aves)) ]

#Ejercicio 4

class MedioDeTransporte:

  def __init__(self, combustible):
    self.combustible = combustible
      
  def cargar_combustible(self, cantidad_combustible):
    self.combustible += cantidad_combustible
    
  def entran_personas(self, personas):
    return personas <= self.maximo_personas()
      
class Moto(MedioDeTransporte):
  
  def maximo_personas(self):
    return 2 
    
  def recorrer(self, kms):
    self.combustible = self.combustible - 1*kms
      
class Auto(MedioDeTransporte):
    
  def maximo_personas(self):
    return 5
  
  def recorrer(self, kms):
    self.combustible = self.combustible - (kms/2)


