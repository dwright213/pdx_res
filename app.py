from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify
import pytumblr, os
from flask_mongokit import MongoKit, Document, Connection


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

connection = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

# mongo stuff
class Blag(Document):
	__collection__ = 'blags'


	structure = {
		'title': unicode,
		'text': unicode,
		'creation': datetime,
	}
	required_fields = ['title', 'creation']
	default_values = {'creation': datetime.utcnow}
	use_dot_notation = True

db = MongoKit(app)
db.register([Blag])
# end mongo stuff

@app.before_request
def set_up_nav():
	g.nav = ['home', 'infos', 'fotos', 'etc']

def tumblr_keys():
	g.client = pytumblr.TumblrRestClient(
	app.config['CONSUMER_KEY'],
	app.config['CONSUMER_SECRET'],
	app.config['OAUTH_TOKEN'],
	app.config['OAUTH_SECRET'])

@app.route('/')
def home():
	# abort(403)
	return render_template('index.html')

@app.route('/blah')
def mongo():
	jason = []
	blags = db.Blag.find()
	for blag in blags:
		jason.append({'title': blag.title, 'text': blag.text})
	return jsonify(jason)

@app.route('/new')
def new_blag():
		blag = db.Blag()
		blag.title = u'this is a test ' + str(datetime.utcnow())
		blag.text = u'this is only a test'
		blag.save()
		return 'okay, blags added'

@app.route('/infos')
def infos():
	return render_template('infos.html')

@app.route('/fotos')
def fotos():
	tumblr_keys()
	posts = g.client.posts(app.config['PHOTO_BLOG'], limit='100', type='photo', filter='text')['posts']
	return render_template('fotos.html', posts=posts)

# @app.route('/fotosobject')
# def fotosobject():
# 	tumblr_keys()
# 	photos = g.client.posts(app.config['PHOTO_BLOG'], limit='10', type='photo', filter='text')['posts']
# 	# return render_template('fotos.html', photos=photos)
# 	return jsonify(photos)

@app.route('/etc')
def etc():
	return render_template('etc.html')

@app.route('/video/therealgundam')
def video():
	return render_template('video.html', video=app.config['GUNDAM_VIDEO'])

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
