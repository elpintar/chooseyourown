# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014
# Database interfacing

import json
from pymongo import MongoClient

class DataBase(object):
	
	def __init__(self):
		# Database names
		dbName = "heroku_app21800319"
		comicsCollectionName = "Comics"
		panalsCollectionName = "Panals"
		self.idField = "id"

		# load settings
		settings = {}
		execfile("dataBaseSettings.conf", settings)
		
		client = MongoClient( settings["URI"] )
		
		# databases
		db = client[dbName]
		self.comicsDB = db[comicsCollectionName]
		self.panalsDB = db[panalsCollectionName]

		print self.getPanalByID(3)
		print self.getComicByID(1)
		print self.getAllComics()

	#==============================================
	# GET Methods
	#==============================================

	def getPanalByID(self, id):
		"""Get panal by ID, return dict"""
		return self.panalsDB.find_one({self.idField:id})

	def getComicByID(self, id):
		"""Get comic by ID, return dict"""
		return self.comicsDB.find_one({self.idField:id})

	def getAllComics(self):
		"""Get all comics and return in list ordered by ID"""
		cur = self.comicsDB.find()
		return list(cur.sort(self.idField))

	#==============================================
	# NEW Methods
	#==============================================

	def newComic(self):
		return 42

	def newPanal(self):
		return 42

	#==============================================
	# UPDATE Methods
	#==============================================

	

DataBase()