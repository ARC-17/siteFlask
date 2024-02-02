from flask import Flask, render_template, request

app = Flask("projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="ARC-17"), 200

@app.route("/tipoget")
def ir_get():
    return render_template("get.html"), 200

@app.route("/receber/", methods=['GET','POST'])
def receber():
    if request.method == 'GET':
        return "Estou no tipo GET!", 200
    elif request.method == "POST":
        return "Estou no tipo POST!", 200
@app.route("/tipopost")
def ir_post():
    return render_template("post.html"), 200
@app.route("/informacao/")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def info(nome = None,idade = None):
    return u"Nome: {}<br>Idade: {}".format(nome,idade), 200

app.run()