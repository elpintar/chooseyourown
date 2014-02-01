# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

'''
API

GET     /                           - home
POST    /                           - create comic
DELETE  /                           - delete comic
GET     /edit?prevID="__"&comID=""  - panel with prevID 
GET     /edit?prevID=""&comID="__"  - initial panel for comID
POST    /edit                       - create panel in database, redirect read
GET     /read?panelID="__"          - display panel
GET     /choose?panelID="__"        - display choose window for given panel
ERROR missing query - redirect home
''' 

import os
import random
from urllib   import quote
from DataBase import DataBase
from bottle   import route, run, template, post, get, delete, static_file, \
                     request, response

#=============================================
# Globals
#=============================================

db = DataBase()

#=============================================
# Home /
#=============================================

@route("/")
def displayMenu():
    # The menu page, displays the list of comics
    comics = db.getAllComics()
    comicList = [(str(cm['startingPanelID']), cm['situation'])
                 for cm in comics]
    return template('menu_template', comicList=comicList)

@post("/")
def createComic():
    situation = request.params['situation']
    id = db.newComic(situation)
    response.headers['Context-Type'] = 'text/plain'
    return str(id)

@delete("/")
def deleteComic():
    comID = request.params['comID']
    db.deleteComic(comID)

#=============================================
# Edit /edit
#=============================================

@route("/edit")
def displayEdit():
    # Returns the edit page
    # TODO add logic for first or continuation
    return template('edit_template')

@post("/edit")
def postEdit():
    # Adds a new panel to the database and returns its ID.
    prevID = request.params.get('prevID')
    comID = request.params.get('comID', '')
    whatIsHappening = request.params.get('whatIsHappening')
    img = request.params.get('img')
    # if no prevID then this is a first panel
    if prevID != None:
        newID = db.newPanel(prevID, comID, whatIsHappening, img)
    else:
        newID = db.newFirstPanel(comID, whatIsHappening, img)
    response.headers['Context-Type'] = 'text/plain'
    return str(newID)

#=============================================
# Read /read
#=============================================

@route("/read")
def displayPanel():
    # Returns the display screen for the given panel
    try:
        panelID = request.query.panelID
    except:
        return displayMenu()
    else:
        pan = db.getPanelByID(panelID)
        img = pan['img']
        prevID = pan.get('prevID','')
        children = pan.get('nextIDs')
        comID = pan.get('comID','')
        whatIsHappening = pan['whatIsHappening']
        numChildren = len(children)
        if numChildren > 0:
            nextID = str(children[0])
        else:
            nextID = ''
        return template('read_template', panelID=panelID, nextID=nextID, 
                        prevID=prevID, numChildren=numChildren, img=img,
                        whatIsHappening=whatIsHappening, comID=comID)

#=============================================
# Choose next panel /choose
#=============================================

@route("/choose")
def displayNext():
    # Returns the next-panel decision screen
    try:
        panelID = request.query.panelID
    except:
        return displayMenu()
    else:
        pan = db.getPanelByID(panelID)
        par = pan['prevID']
        comID = pan.get('comID', '')
        com = db.getComicByID(comID)
        storyStart = com.get('startingPanelID','')
        all_children = pan['nextIDs']
        children = [(str(ch_id), db.getPanelByID(ch_id)['whatIsHappening']) 
                    for ch_id in all_children]
        return template('choose_template', panelID=panelID, children=children, storyStart=storyStart)

#=============================================
# Static files
#=============================================

# What follows is copied from the Internet.
# Thank you Internet.
# http://stackoverflow.com/questions/10486224/bottle-static-files
@get('/static/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/static/css/<filename:re:.*\.(css|woff|ttf)>')
def stylsheets(filename):
    return static_file(filename, root='static/css')

@get('<filename:re:.*\.html>')
def stylsheets(filename):
    return static_file(filename, root='views')

@get('/static/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

#=============================================
# Serve site
#=============================================

if 'RUNNING_HEROKU' in os.environ:
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8000)
