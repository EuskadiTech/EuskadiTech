from flask import Flask, render_template, send_file
from AulaSDK import auth, food_filter, taskassign_filter
from os import environ
from gtts import gTTS

app = Flask(__name__)


@app.route('/r/<int:aula>')
def resumen(aula: int):
    a = auth(environ["ET_USER"],environ["ET_PASSWORD"])
    return render_template("resumen.html", l = food_filter(a, aula), tasks = taskassign_filter(a, aula))

@app.route('/tts/<int:aula>')
def tts(aula: int):
    a = auth(environ["ET_USER"],environ["ET_PASSWORD"])
    tts = gTTS(render_template("resumen.txt", l = food_filter(a, aula), tasks = taskassign_filter(a, aula)), lang="es")
    tts.save("/tmp/aulatts.mp3")
    return send_file("./data/tts.mp3")

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/c/<int:aula>')
def comedor(aula: int):
    a = auth(environ["ET_USER"],environ["ET_PASSWORD"])
    return render_template("comedor.html", l = food_filter(a, aula))
if __name__ == "__main__":
    app.run("0.0.0.0", "18881", debug=True)