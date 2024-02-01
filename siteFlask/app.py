from flask import Flask, render_template

app = Flask("projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="ARC-17"), 200

@app.route("/informacao/")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def info(nome = None,idade = None):
    return u"Nome: {}<br>Idade: {}".format(nome,idade), 200

app.run()