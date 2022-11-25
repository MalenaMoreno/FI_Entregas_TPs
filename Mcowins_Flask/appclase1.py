from flask import Flask, render_template
from markupsafe import escape 

app = Flask(__name__)

prendas = {
100: { "Tipo": "Pantalón", "Talle": "S"},
101: { "Tipo": "Remera", "Talle": "M"}
}


@app.get("/")       #home # url de escucha
def home():
    return "Bienvenido a Macowins!"

@app.get("/prendas/")
def get_prendas():
    return render_template("prendas.html", prendas = prendas.items())

@app.get("/prendas/<int:id>")
def get_prenda(id):
    if id in prendas:
        prenda = prendas[id]
        return render_template("prenda.html", id=id, prenda=prenda)
    else:
        return f"No se encuentra la prenda. Error 404"


