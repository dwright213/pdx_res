from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, url_for
import pytumblr, os
import requests, json, xmltodict

def medium_xml_get():
	url = 'https://medium.com/feed/@pdxresistance'
	r = requests.get(url)
	return r.text

def transmogrify(medium_feed):
	post_list = []
	posts = medium_feed['rss']['channel']['item']
	for post in posts:
		current = {}
		current['title'] = post['title']
		current['body'] = post['content:encoded']
		current['link'] = post['link']
		current['date'] = post['pubDate']
		current['tags'] = post['category']
		post_list.append(current)

	return post_list

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


@app.route('/xml_post')
def xml_post():
	data = xmltodict.parse(medium_xml_get())
	posts = transmogrify(data)
	return jsonify(posts)



if __name__ == "__main__":
	app.run(host='0.0.0.0')
