
import requests

"""
Hacemos el pedido que se dispara cuando yo hago el clic, que pasa detrás?

Vamos a trabajar con la aplicacion "macowins", tiene de juguete info que representa un comercio de venta de ropa 

https://macowins-server.herokuapp.com/prendas/1 
https: --> protocolo
macowins-server.herokuapp.com --> dominio 
prendas/1  --> primer item del recurso prendas 

HTTP --> tiene verbbos que me dicen que estoy hacinedo con los recursos 
"""

r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(r.json())
#devuelve --> {'id': 1, 'tipo': 'pantalon', 'talle': 35}


"""
Que hace get? --> verbo http qu ese usa para hacer los pedidos al servidor 
requests.get --> conectate a esta url y traeme lo que puedas traerme

Que hace .json? --> estructurar el resultado en un formato legible al ojo humano
Es un formato de datos y en terminos de python se parece a un diccionario 
"""

import requests

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
with open ("bio.txt", "a") as salida:
    salida.write(str(pikachu.json()))





