from flask import Flask, render_template, url_for, jsonify, request
from form import InputFieldForm, Randomizer
import json, urllib.request
from filter_tool import search
from randomizer import randomizer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

@app.route('/')
def index_page():
	form = InputFieldForm()
	form2 = Randomizer()
	return render_template('index.html', form=form, form2=form2)

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		inputs = request.form.to_dict()
		searchword = inputs["searchword"]
		results = search(inputs)

	return render_template("result.html", searchword= searchword, results=results)


@app.route('/random')
def random():
	results = randomizer()
	name = "Randomly Generated Question"
	return render_template("randomizer.html", results=results, name=name)

