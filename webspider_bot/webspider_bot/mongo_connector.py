from webspider_bot import settings 
from pymongo import MongoClient

# Create a connection the hosted MongoDB
client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DATABASE]

def fetch_article_link(filter=None):
	all_article_link = []
	for data in db.articles.find():
		all_article_link.append(data['article_link'])
	return all_article_link