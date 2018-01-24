# -*- coding=utf8 -*-
from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost:27017'

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client['jiayuan']
mongo_collection = mongo_db['user']

