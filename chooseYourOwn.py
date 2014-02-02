# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

'''
API

GET     /                            - home
GET     /edit?situation="__"         - initial panel in new comic wth given situation 
GET     /edit?prevID="__"&comID="__" - previous panel with comID
POST    /edit                        - create panel in database, redirect read
GET     /read?panelID="__"           - display panel
GET     /choose?panelID="__"         - display choose window for given panel
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

#=============================================
# Edit /edit
#=============================================

@route("/edit")
def displayEdit():
    # Returns the edit page
    return template('edit_template')

@post("/edit")
def postEdit():
    # either create a new comic and panel or create a continuation panel
    prevID          = request.params.get('prevID')
    whatIsHappening = request.params.get('whatIsHappening')
    img             = request.params.get('img')
    situation       = request.params.get('situation')

    if prevID == None:
        # if no prevID then this is a first panel
        # create new comic and panel
        comID = db.newComic(situation)
        newID = db.newFirstPanel(comID, whatIsHappening, img)
    
    else:
        # pull comID from the previous panal
        prev = db.getPanelByID(prevID)
        comID = prev.get('comID', '')
        newID = db.newPanel(prevID, comID, whatIsHappening, img)

    # return id of panel
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
        img = pan.get('img', '')
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
        
        children = []
        for ch_id in all_children:
            cPanel = db.getPanelByID(ch_id)
            if cPanel != None:
                children.append( (str(ch_id), cPanel['whatIsHappening'] ) )
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
