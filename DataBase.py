# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014
# Database interfacing

import json
from pymongo import MongoClient
from bson.objectid import ObjectId

class DataBase(object):
    """DatBase instantiates a connection to our dataBase and performs queries"""

    def __init__(self):
        # Database names
        dbName = "heroku_app21800319"
        comicsCollectionName = "Comics"
        panelsCollectionName = "Panels"
        self.idField = "_id"
        self.nextIDField = "nextIDs"
        self.firstPanelIDField = "startingPanelID"

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
        """Get panal by ID, return dict and None on error"""
        if not ObjectId.is_valid(_id):
            return None
        return self.panelsCollection.find_one({self.idField : ObjectId(_id)})

    def getComicByID(self, _id):
        """Get comic by ID, return dict and None on error"""
        if not ObjectId.is_valid(_id):
            return None
        return self.comicsCollection.find_one({self.idField : ObjectId(_id)})

    def getAllComics(self):
        """Get all comics and return in list ordered by ID or None on error"""
        if not ObjectId.is_valid(_id):
            return None
        cur = self.comicsCollection.find()
        return list(cur.sort(self.idField))

    #==============================================
    # NEW Methods
    #==============================================

    def newComic(self, situation):
        """create a new comic given the arguments,
            generates a unique _id. Returns _id"""
        return self.comicsCollection.insert( { "situation": situation,
                                       "startingPanelID" : None })

    def newPanel(self, prevID, whatIsHappening, img):
        """create a new panal given the arguments,
            generates a unique _id. Returns _id and None on error.
            Also updates the prevID to point to the 
            new ID"""
        if not ObjectId.is_valid(prevID):
            return None

        newID = self.panelsCollection.insert( { "prevID": prevID,
                                       "whatIsHappening" : whatIsHappening,
                                       "nextIDs" : [],
                                       "img" : img })
        # update prev to point to new
        if (self._updateNextIDs(prevID, newID) == True):
            return newID
        return None

    def newFirstPanel(self, comicID, whatIsHappening, img):
        """create a new panal given the arguments,
            generates a unique _id. Returns _id and None on error.
            Also updates the comic to point to the 
            new panel ID"""
        if not ObjectId.is_valid(comicID):
            return None

        # prevID is not present as this is first panel in comic
        newID = self.panelsCollection.insert( { "prevID": None,
                                       "whatIsHappening" : whatIsHappening,
                                       "nextIDs" : [],
                                       "img" : img })
        # update comic to point to newID as the startingPanelID
        if (self._updateStartingPanelID(comicID, newID) == True):
            return newID
        return None # error in updating


    #==============================================
    # UPDATE Methods
    #==============================================

    def _updateNextIDs(self, frameID, nextFrameID):
        """This is a private method.
           Add the nextID to the given frame id,
           return true if successful, false otherwise"""
        if (not ObjectId.is_valid(frameID)) or (not ObjectId.is_valid(frameID)):
            return False

        frameDoc = self.panelsCollection.find_one( {self.idField : 
                                                        ObjectId(frameID)} )
        if frameDoc == None:
            return False

        nextIDs = frameDoc["nextIDs"]
        nextIDs.append(nextFrameID)
        nextIDs = list(set(nextIDs)) # only unique next panels

        if( self.panelsCollection.update( { self.idField : ObjectId(frameID)}, 
                        { "$set" : {self.nextIDField : nextIDs} }) != None):
            return True
        return False # update unsuccessful 

    def _updateStartingPanelID(self, comicID, firstPanelID):
        """This is a private method.
           Add the firstPanelID to the given comic as the starting panel,
           return true if successful, false otherwise"""
        if (not ObjectId.is_valid(comicID)) or (not ObjectId.is_valid(firstPanelID)):
            return False

        if (self.comicsCollection.find_and_modify({self.idField: ObjectId(comicID)}, 
                {"$set" : {self.firstPanelIDField : firstPanelID} }) != None):
            return True
        return False # update unsuccessful

#$%&&^#$&*^#$%^@&Q*$*$#^%&&^$^^%&^#$^#%%&^#@%*&$#(*@#(*$*))
# WARNING WARNING YOU ARE ENTERING THE SCARY ZONE
# ENTER AT YOUR OWN HAZARD -- YOU MAY NOT RETURN
#$%&&^#$&*^#$%^@&Q*$*$#^%&&^$^^%&^#$^#%%&^#@%*&$#(*@#(*$*))

    #==============================================
    # DELETE Methods
    #==============================================

    def deleteComic(self, _id):
        """Delete comic with given ID. 
           Return True on success, false otherwise"""
        if not ObjectId.is_valid(_id):
            return False
        try:
            self.comicsCollection.remove({self.idField : ObjectId(_id)})
            return True
        except  pymongo.errors.OperationFailure as E:
            return False

    def deletePanel(self, _id):
        """Delete panel with given ID. 
           Return True on success, false otherwise"""
        if not ObjectId.is_valid(_id):
            return False
        try:
            self.panelsCollection.remove({self.idField : ObjectId(_id)})
            return True
        except  pymongo.errors.OperationFailure as E:
            return False