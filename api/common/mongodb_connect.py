from pymongo import MongoClient
from settings import *

class MongoDBConnect(object):

	#
	# Create a connection the hosted MongoDB
	#
	
	client = MongoClient(MONGODB_URI)
	db = client[MONGODB_DATABASE]