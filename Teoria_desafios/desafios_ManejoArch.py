
# Desafío I: Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.

archivo = open("bio.txt", "w")
archivo.close()

# Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()

# Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación.

with open("bio.txt", "w") as archiv:
    archiv.write("Hola que tal\nSoy Malena Moreno\nTengo 19 años.")

# Para pensar 🤔:¿Cómo darías formato al texto que estas creando?

# Desafio IV: Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido
# y lo imprima en pantalla el resultado

with open("manipulacion_archivos.txt", "r") as archiv:
    print(archiv.read())