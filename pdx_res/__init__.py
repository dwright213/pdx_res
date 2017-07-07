from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, url_for

from twitter import *
from ttp import ttp
import facebook
from facebook import GraphAPI

import os
import requests, json, xmltodict, time, timeago

app = Flask(__name__)
app.config.from_pyfile('../settings.cfg')


# medium stuff can chill here for now
def medium_xml_get():
	url = 'https://medium.com/feed/@pdxresistance'
	r = requests.get(url)
	return r.text

def transmogrify(medium_feed):
	post_list = []
	posts = medium_feed['rss']['channel']['item']
	for post in posts:
		current = {}
		date = datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S GMT').strftime('%b %-d, %Y')
		current['title'] = post['title']
		current['body'] = post['content:encoded']
		current['link'] = post['link']
		current['date'] = date
		current['tags'] = post['category']
		post_list.append(current)
	return post_list


# twitter stuff can squat here for the time being
twitter = Twitter(auth=OAuth(\
	app.config['TWITTER_TOKEN'],\
	app.config['TWITTER_TOKEN_SECRET'],\
	app.config['TWITTER_CONSUMER_KEY'],\
	app.config['TWITTER_CONSUMER_SECRET']))

# facebook stuff can reside here
fbtoken = app.config['FB_TOKEN']
graph = facebook.GraphAPI(access_token=fbtoken, version='2.7')

# jinja filter hanging around here momentarily
@app.template_filter()
def format_date(date_string):
	date = datetime.strptime(date_string, '%a %b %d %H:%M:%S +0000 %Y')
	time_since = timeago.format(date)
	return time_since

@app.template_filter()
def format_iso(date_string):
	date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S+0000')
	time_since = timeago.format(date)
	return time_since



@app.before_request
def set_up_nav():
	g.nav = ['home', 'who', 'about', 'connect']

@app.route('/')
def home():
	return render_template('page/index.html')

@app.route('/about')
def about():
	data = xmltodict.parse(medium_xml_get())
	posts = transmogrify(data)
	return render_template('page/about.html', posts=posts)


@app.route('/xml_post')
def xml_post():
	data = xmltodict.parse(medium_xml_get())
	posts = transmogrify(data)
	return jsonify(data)

@app.route('/workgroups/<group>')
def workgroups(group):
	return render_template('page/%s.html' % group)

@app.route('/tweets')
def tweets():
	tweets = twitter.statuses.user_timeline(screen_name='pdx_resistance', count=20)
	tweetpile = {
		'title': 'hey heres some tweetz',
		'tweets': tweets
	}
	return jsonify(tweetpile)

@app.route('/fb_events')
def fb_events():
	page_id = app.config['FB_ID']
	events = graph.get_object(id=page_id,fields='about,events.limit(10)')
	return jsonify(events)

@app.route('/fb_posts')
def fb_status():
	page_id = app.config['FB_ID']
	statuspile = graph.get_object(id=page_id,fields='posts.limit(10){link,message,full_picture,picture,description,caption,name,type,created_time},picture')

	statuses = statuspile['posts']['data']
	for status in statuses:
		try:
			desc = status['description'].encode('ascii', 'ignore')
			print(len(desc))
			if len(desc) > 255:
				print('oops, thhis is  a long one')
				split_desc = desc.split(' ')
				print(len(split_desc))
				for index, word in enumerate(split_desc):
					if index > 25:
						

				print('''

					''')

		except:
			print('no descriptions here...')

	return jsonify(statuspile)

@app.route('/connect')
def connect():
	page_id = app.config['FB_ID']
	statuspile = graph.get_object(id=page_id,fields='posts.limit(10){link,message,full_picture,picture,description,caption,name,type,created_time},picture')


	tweetpile = twitter.statuses.user_timeline(screen_name='pdx_resistance', count=10)
	for tweet in tweetpile:
		text = tweet['text'].encode('ascii', 'ignore')		
		p = ttp.Parser()
		result = p.parse(text)
		tweet['text_parsed'] = result.html

	return render_template('page/connect.html', tweets=tweetpile, statuses=statuspile['posts']['data'], fb_pic=statuspile['picture']['data']['url'])


if __name__ == "__main__":
	app.run(host='0.0.0.0')
