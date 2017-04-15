from datetime import datetime
from flask import Flask, render_template, request, g, abort, jsonify, url_for
from twitter import *
import pytumblr, os
import requests, json, xmltodict, time


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

	# fetch 3 tweets from ITP_NYU
	# itpTweets = twitter.statuses.user_timeline(screen_name='itp_nyu', count=10)
	
	# # app.logger.debug(itpTweets)


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
	tweets = twitter.statuses.user_timeline(screen_name='cbeckpdx', count=20)
	tweetpile = {
		'title': 'hey heres some tweetz',
		'tweets': tweets
	}          
	return jsonify(tweetpile)

@app.route('/connect')
def connect():
	tweetpile = twitter.statuses.user_timeline(screen_name='pdx_resistance', count=20)
	return render_template('page/connect.html', tweets=tweetpile)


if __name__ == "__main__":
	app.run(host='0.0.0.0')
