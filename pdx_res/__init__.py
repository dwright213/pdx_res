from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, url_for
import pytumblr, os
import requests, json, xmltodict

def medium_get():
	url = 'https://medium.com/_/api/users/113dce49fa97/profile/stream'
	headers = {'Accept': 'application/json'}
	r = requests.get(url, headers=headers)
	clean_response = r.text.replace('])}while(1);', '').replace('</x>', '')
	return clean_response

def medium_post_get():
	url = 'https://medium.com/_/api/posts/a1aeb9667525'
	r = requests.get(url)
	return r.text

def medium_xml_get():
	url = 'https://medium.com/feed/@pdxresistance'
	headers = {'Accept': 'application/json'}
	r = requests.get(url, headers=headers)
	clean_response = r.text.replace('])}while(1);', '').replace('</x>', '')
	return clean_response


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

@app.route('/posts')
def posts():
	cooked_json = json.loads(medium_get())
	all_posts = cooked_json['payload']['references']['Post']
	return jsonify(all_posts)

@app.route('/a_post')
def a_post():
	cooked_json = json.loads(medium_post_get())
	return jsonify(cooked_json)

@app.route('/xml_post')
def xml_post():
	data = medium_xml_get()
	parsedx = xmltodict.parse(data)
	return jsonify(parsedx)



@app.route('/post/<post_id>')
# @app.route('/post')
def post(post_id):
	cooked_json = json.loads(medium_get())
	all_posts = cooked_json['payload']['references']['Post']

	# print(dir(all_posts))
	post_keys = all_posts.keys()
	chosen_key = post_keys[int(post_id)]
	chosen_post = all_posts[chosen_key]
	post_title = chosen_post['title']
	post_subtitle = chosen_post['virtuals']['subtitle']
	post_meta = chosen_post['virtuals']['metaDescription']

	digested = {'title': post_title, 'subtitle': post_subtitle, 'meta': post_meta }

	# https://medium.com/_/api/posts/4114cd73ba5c
	# will get us the post, with id 4114cd73ba5c.
	return jsonify(digested)


if __name__ == "__main__":
	app.run(host='0.0.0.0')
