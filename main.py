from flask import Flask, render_template

app = Flask(__name__)

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html",nome_usuario=nome_usuario)

if __name__=="__main__":
    app.run(port=10000, host='0.0.0.0', debug=True)
