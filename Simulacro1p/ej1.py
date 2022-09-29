# Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'.
# Por ejemplo para XbaaaYjXababYqXbabbbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].

import re

patron = "X(.*?ab.*?)Y" #signo de preg favorecer matches internos

patron_ok = "X([^X]*?ab[^Y].*?)Y"

def funcion1(string):
    print(re.findall(patron_ok, string))

funcion1("XbaaaYjXababYqXbabbbbaaYqXffeeY")

# . cualquier carac 
# * 0 o mas veces
# ? matches internos --> que mire adentro y no solo los bordes


# Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer
# la lista de substrings delimitadas por los patrones 'ag' y 'cta', no incluyan números.
# Revisá su código propuesto y marcá con una `x` las opciones correctas. JUSTIFICA tus respuestas.

import re

def funcionDeExpresiones_Regulares(string):
    print(re.findall("ag(\d.*?)cta", string))

funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta')


def entre_ag_y_cta_sin_numeros2(string):
    print(re.findall("ag([^\d]*)cta", string))

entre_ag_y_cta_sin_numeros2('aabocaggaaactazu4lggaasag24gra1ndecta')
