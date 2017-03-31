from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify
import pytumblr, os
from flask_mongokit import MongoKit, Document, Connection


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

@app.before_request
def set_up_nav():
	g.nav = ['home']

@app.route('/')
def home():
	# abort(403)
	return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
