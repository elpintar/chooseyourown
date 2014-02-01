# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014
# Database interfacing

import json
from pymongo import MongoClient

class DataBase(object):
	
	def __init__(self):
		settings = {}
		execfile("dataBaseSettings.conf", settings)
		
		self.db = MongoClient( settings["URI"] )

	def getPanal():
		return 42


DataBase()