from flask import Flask, render_template
from AulaSDK import auth, food_filter
from os import environ
app = Flask(__name__)


@app.route('/r/<aula>')
def index(aula):
    return render_template("resumen.html", l = food_filter(auth(environ["ET_USER"],environ["ET_PASSWORD"]), aula))

 
@app.route('/c/<int:aula>')
def comedor(aula: int):
    return render_template("comedor.html", l = food_filter(auth(environ["ET_USER"],environ["ET_PASSWORD"]), aula))
if __name__ == "__main__":
    app.run("0.0.0.0", "18881", debug=True)