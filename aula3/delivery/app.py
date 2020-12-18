from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "<h1>Ola, Codeshow Thiago<h1>"

@app.route("/sobre")
def sobre():
    return "<p>Este é melhor site de delivery do mundo <p>"

