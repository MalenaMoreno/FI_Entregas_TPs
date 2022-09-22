
# MODELO EJERCICIO POO

# Salud titanes (100 de máxima)
# Puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere.
# 
# Al recibir ataque la salud disminuye 1.5 por cada puntos de daño recibido.

# Tienen la capacidad de destruir cierto número de casas dependiendo de su salud,

# Destruyen 8 casas cuando su salud es máxima 
# Destruyen un número proporcional si su salud es menor a la máxima (100)

# (si tiene 60 puntos de salud destruye 4.8 casas, es decir, 4 casas completas y más de la mitad de otra).
# 
# Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!",
# el único sonido que hacen.

# Definí la clase Titan con los atributos y métodos correspondientes.
# Además instanciá a un Titan y ejecutá las siguientes líneas:

'''
titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())       # True
print(titan1.salud_actual())    # 55
print(titan1.cuantas_casas())    # 4.4
print(titan1.grito())           # "¡Aaaarrrg!"
titan1.destruir_casas()
titan1.salud_actual()           # 5.0
titan1.recibir_ataque(4)
print(titan1.esta_vivo()) # False


'''

class Titan:

    def __init__(self, salud):
        self.salud = salud
    
    def salud_actual(self):
        return self.salud

    def recibir_ataque(self, puntos):
        self.salud -= 1.5 * puntos
    
    def esta_vivo(self):
        return self.salud > 0

    def cuantas_casas(self):
        return (self.salud * 8 / 100)

    def destruir_casas(self):
        if (self.cuantas_casas() > 1):
            if ((self.cuantas_casas() % 1) > 0):
                self.salud -= (self.cuantas_casas() // 1) * 12.5
            else:
                self.salud -= (self.cuantas_casas() - 1) * 12.5
        else:
            print("No puede destruir ninguna casa")

    def grito(self):
        return "¡Aaaarrrg!"

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())       # True
print(titan1.salud_actual())    # 55
print(titan1.cuantas_casas())    # 4.4
print(titan1.grito())           # "¡Aaaarrrg!"
titan1.destruir_casas()
titan1.salud_actual()           # 5.0
titan1.recibir_ataque(4)
print(titan1.esta_vivo())
