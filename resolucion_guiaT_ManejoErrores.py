# Desafio I: Descargá y ejecutá el script1_manejo_errores.py
#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa?
# ¿En dónde se encuentra el error? ¿Cómo te das cuenta? --> esta en el script de la clase

#DESAFIO I
# Hecho en clase (del script1_manejo_errores.py)

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 0
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# try: 
#     # find two solutions
#     sol1 = (-b-cmath.sqrt(d))/(2*a)
#     sol2 = (-b+cmath.sqrt(d))/(2*a)
#     print('The solution are {0} and {1}'.format(sol1,sol2))
# except ZeroDivisionError:                                                         #cualquier error que salga, hace esto
#     print ("Zero Division is not allow, check a value")
#     pass   #abajo del error el codigo sigue corriendo 
# print("ya esta")
#     # print("ya esta") --> esta mal aca esto 

# if a != 0:
#     sol1 = (-b-cmath.sqrt(d))/(2*a)
#     sol2 = (-b+cmath.sqrt(d))/(2*a)
#     print('The solution are {0} and {1}'.format(sol1,sol2))
# elif a == 0:
#     raise TypeError("a can`t be 0")

if a == 0:
    raise TypeError("a can`t be 0")
else:
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))

## Desafio II: Creá una función denominada mitades que tenga como argumento un número e
# imprima el resultado de la división de ese número por 2

def mitades(numero):
    print(numero/2)

mitades(9)

mitades(0) # ??????

# Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0? 

# Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero?
# Reescribí la función incorporando una declaración try-except
