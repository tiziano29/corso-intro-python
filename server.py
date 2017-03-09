from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



@app.route('/saluta')
def saluta(nome):
	return 'ciao %s' % nome

@app.route('/somma/<int:a>/<int:b>')
def somma (a, b):
	somma = a + b
	return "%s" % somma


@app.route ('auto/<nome>/<anno>/<marca>/<consumo>')
def crea_automobile(nome, anno, marca, consumo):
	auto=Automobile(nome, anno ,marca, comsumo)
	return auto






app.run()
