from flask import Flask, render_template

app = Flask("projeto")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="ARC-17"), 200

app.run()