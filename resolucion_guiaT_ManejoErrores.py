# Desafio I: Descargá y ejecutá el script1_manejo_errores.py
#Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa?
# ¿En dónde se encuentra el error? ¿Cómo te das cuenta? --> esta en el script de la clase


## Desafio II: Creá una función denominada mitades que tenga como argumento un número e
# imprima el resultado de la división de ese número por 2

def mitades(numero):
    print(numero/2)

mitades(9)

mitades(0) # ??????

# Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0? 

# Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero?
# Reescribí la función incorporando una declaración try-except
