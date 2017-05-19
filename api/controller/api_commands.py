
from pymongo import MongoClient
from common.settings import *
from common.mongodb_connect import MongoDBConnect

mongo = MongoDBConnect.db

def test_route():
	return jsonify({'result' : 'This is a test route!'})

def search_key(keyword=None):
	
	if not keyword:
		return {
					'result': [],
					'help': 'provide keyword for search. eg. /search/<keyword>'
				}
	
	output = []	
	articles = mongo.articles
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

	return {'result':output}


def search_specific(attribute=None, keyword=None):

	# verify attribute and keyword
	if not attribute or not keyword:
		return 	{
					'result':[],
					'help':'provide the ff. syntanx  eg. \'/search/<tag>/<keyword>\''
				}
		
	# construct specific filter query
	query_filter = _search_query_by_filter(keyword,attribute)
	
	output = []	
	articles = mongo.articles	
	for q in articles.find(query_filter):	
		output.append({
			'article_link': q['article_link'],
			'category': q['category'],
			'author' : q['author'],
			'headline': q['headline'],
			'content': q['content'],
			'date': q['date']
		})

	return {'result':output}


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