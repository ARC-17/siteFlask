from flask import Flask, render_template, request, session, redirect

app = Flask("projeto")
app.secret_key = 'Minha_chave'
@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="ARC-17"), 200

@app.route("/tipoget")
def ir_get():
    return render_template("get.html"), 200

@app.route("/receber/", methods=['GET','POST'])
def receber():
    if request.method == 'GET':
        return "Estou no tipo GET!<br>Nome: {} <br>Idade: {}".format(request.args.get("nome"),request.args.get("idade")), 200
    elif request.method == "POST":
        return "Estou no tipo POST!<br>Nome: {} <br>Idade: {}".format(request.form["nome"],request.form["idade"]), 200
@app.route("/tipopost")
def ir_post():
    return render_template("post.html"), 200
@app.route("/informacao/")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")
def info(nome = None,idade = None):
    return u"Nome: {}<br>Idade: {}".format(nome,idade), 200
@app.route("/sessao/")
def acesso_sessao():
    return '''
        <h1>inicio da Sessão</h1>
        <form action="{}" method="post" >
            Usuário: <input type="text" name="usuario"/>
            <br/>
            <input type="submit" value="Acesso restrito"/>
        </form>
    '''.format(url_for('validacao_sessao')), 200

@app.route("/validacao/", methods=['POST'])
def validacao_sessao():
    if request.method == "POST":
        session['usuario'] = request.form["usuario"]
        return redirect(url_for('acesso_restrito'))

    return redirect(url_for('acesso_sessao'))
@app.route("/restrito/")
def acesso_restrito():
    if ( session['usuario'] ):
        return "Estou na área de acesso restrito!", 200

    return redirect(url_for('acesso_sessao'))

app.run()