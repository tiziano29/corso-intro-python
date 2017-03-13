from flask import Flask, render_template,request
from oggetti import Automobile
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


"""
@app.route('/saluta')
def saluta(nome):
	return 'ciao %s' % nome
"""

@app.route('/somma/<int:a>/<int:b>')
def somma (a, b):
	somma = a + b
	return "%s" % somma


@app.route ('/auto/<nome>/<anno>/<marca>/<consumo>')
def crea_automobile(nome, anno, marca, consumo):
	auto=Automobile(nome, anno ,marca, comsumo)
	return auto

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


@app.route('/saluta', methods=['POST','GET'])
def saluta():
	name = request.form['name']
	return render_template('*saluta.html', name=name)

@app.route8 ('/nuovaauto')
def nuovaauto():
	return render_template('nuovauato.html')

@app.route8 ('/salvaauto',method =["POST"])
def salvaauto():
	nome = request.form['name']
	anno = request.form['year']
	marca = request.form['brand']
	consumo = request.form['compustion']

	auto = Automobile(nome, anno, marca, consumo)
	
	return return render_template('salvauto.html', name = auto,nome)
	



app.run()
