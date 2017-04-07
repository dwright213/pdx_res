from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, url_for
import pytumblr, os
from flask_mongokit import MongoKit, Document, Connection


app = Flask(__name__)
app.config.from_pyfile('../settings.cfg')

@app.before_request
def set_up_nav():
	g.nav = ['home', 'who', 'about', 'connect']

@app.route('/')
def home():
	return render_template('page/index.html')

@app.route('/about')
def about():
	return render_template('page/about.html')



if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0')
