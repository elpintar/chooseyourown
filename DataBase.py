# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014
# Database interfacing

import json
from pymongo import MongoClient
from bson.objectid import ObjectId

class DataBase(object):
	"""DatBase instantuates a conncetion to our dataBase and performs queries"""

	def __init__(self):
		# Database names
		dbName = "heroku_app21800319"
		comicsCollectionName = "Comics"
		panelsCollectionName = "Panels"
		self.idField = "_id"
		self.nextIDField = "nextIDs"

		# load settings
		settings = {}
		execfile("dataBaseSettings.conf", settings)
		
		client = MongoClient( settings["URI"] )
		
		# collections
		db = client[dbName]
		self.comicsCollection = db[comicsCollectionName]
		self.panelsCollection = db[panelsCollectionName]

	#==============================================
	# GET Methods
	#==============================================

	def getPanelByID(self, _id):
		"""Get panal by ID, return dict"""
		return self.panelsCollection.find_one({self.idField : ObjectId(_id)})

	def getComicByID(self, _id):
		"""Get comic by ID, return dict"""
		return self.comicsCollection.find_one({self.idField : ObjectId(_id)})

	def getAllComics(self):
		"""Get all comics and return in list ordered by ID"""
		cur = self.comicsCollection.find()
		return list(cur.sort(self.idField))

	#==============================================
	# NEW Methods
	#==============================================

	def newComic(self, situation, startingPanelID):
		"""create a new comic given the arguments,
			generates a unique _id. Returns _id"""
		return self.comicsCollection.insert( { "situation": situation,
									   "startingPanelID" : startingPanelID })

	def newPanel(self, prevID, whatIsHappening, img):
		"""create a new panal given the arguments,
			generates a unique _id. Returns _id.
			Also updates the prevID to point to the 
			new ID"""
		newID = self.panelsCollection.insert( { "prevID": prevID,
									   "whatIsHappening" : whatIsHappening,
									   "nextIDs" : [],
									   "img" : img })
		# update prev to point to new
		self._updateNextIDs(prevID, newID)
		return newID

	#==============================================
	# UPDATE Methods
	#==============================================

	def _updateNextIDs(self, frameID, nextFrameID):
		"""This is a private method.
		   Add the nextID to the given frame id,
		   return true if successful, false otherwise"""
		frameDoc = self.panelsCollection.find_one( {self.idField : ObjectId(frameID)} )
		if frameDoc == None:
			return False

		nextIDs = frameDoc["nextIDs"]
		nextIDs.append(nextFrameID)
		nextIDs = list(set(nextIDs)) # only unique next panels

		self.panelsCollection.update( { self.idField : ObjectId(frameID)}, 
									  { "$set" : {self.nextIDField : nextIDs} })
		return True
