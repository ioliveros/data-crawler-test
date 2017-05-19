from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo
from common.settings import *

app = Flask(__name__)
app.config['MONGO_DBNAME'] = MONGODB_DATABASE
app.config['MONGO_URI'] = MONGODB_URI

mongo = PyMongo(app)

@app.route('/')
def test_route():
	return jsonify({'result' : 'This is a test route!'})


@app.route('/search/')
@app.route('/search/<keyword>', methods=['GET'])
def search_key(keyword=None):

	if not keyword:
		return jsonify({'result': [],
						'help': 'provide keyword for search. eg. /search/<keyword>'
						})
	
	output = []	
	articles = mongo.db.articles
	query_filter = _search_query_by_filter(keyword)
	
	for q in articles.find(query_filter):	
		output.append({
			'article_link': q['article_link'],
			'category': q['category'],
			'author' : q['author'],
			'headline': q['headline'],
			'content': q['content'],
			'date': q['date']
		})

	return jsonify({'result':output})


@app.route('/search/<attribute>/<keyword>',  methods=['GET'])
def search_specific(attribute=None, keyword=None):

	# verify attribute and keyword
	if not attribute or not keyword:
		return jsonify({
					'result':[],
					'help':'provide the ff. syntanx  eg. \'/search/<tag>/<keyword>\''
					})
		
	# construct specific filter query
	query_filter = _search_query_by_filter(keyword,attribute)
	
	output = []	
	articles = mongo.db.articles	
	for q in articles.find(query_filter):	
		output.append({
			'article_link': q['article_link'],
			'category': q['category'],
			'author' : q['author'],
			'headline': q['headline'],
			'content': q['content'],
			'date': q['date']
		})

	return jsonify({'result':output})


def _search_query_by_filter(keyword=None, attribute=None, filter_query={}):

	if not keyword: return filter_query

	if keyword and attribute:
		filter_query = { 
				"$or": [ 
							{ attribute: {'$regex': keyword} }, 						
						] 
					}
	else:
		filter_query = { 
				"$or": [ 
							{ 'article_link': {'$regex': keyword} }, 
							{ 'category': {'$regex': keyword} },
							{ 'author': {'$regex': keyword} },
							{ 'headline': {'$regex': keyword} },
							{ 'content': {'$regex': keyword} },
							{ 'date': {'$regex': keyword} }
						] 
					}

	return filter_query

if __name__ == '__main__':
	app.run(debug=True)