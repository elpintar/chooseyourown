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
# Helper Functions
#=============================================

def comBut(situation, panelID):
    # Return the button containing described with text, situation,
    # and links to /read/panelID
    return ('<a class="choice" href=\"'+ '/read/?panelID=' +
            str(panelID) + '\">' + situation + '</a>' + '\n')

#=============================================
# Home /
#=============================================

@route("/")
def displayMenu():
    # The menu page, displays the list of comics
    comics = db.getAllComics()
    comList = ''
    for cm in comics:
        comicName = quote(cm['situation'].replace(' ', '-'))
        comList += comBut(cm['situation'], cm['startingPanelID'])
    return template('menu_template', comicList = comList)

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
    prevID = request.params['prevID']
    comID = request.params['comID']
    whatsHappening = request.params['whatsHappening']
    img = request.params['img']
    if prevID != '':
        newID = newPanel(prevID, whatsHappening, img)
    else:
        newID = db.newFirstPanel(comID, whatsHappening, img)
    response.headers['Context-Type'] = 'text/plain'
    return str(newID)

#=============================================
# Read /read
#=============================================

@route("/read")
def displayPanel():
    # Returns the display screen for the given panel
    try:
        panel = request.query.panelID
    except:
        return displayMenu()
    else:
        pan = db.getPanelByID(panel)
        img = pan['img']
        par = pan['prevID']
        children = pan['nextIDs']
        if len(children) == 0:
            nextLink = '/edit?prevID=' + panel
        elif len(children) == 1:
            nextLink = '/read?panelID=' + children[0]
        else:
            nextLink = '/choose?prevID=' + panel
        return template('read_template', nextLink=nextLink, parent=par, img=img)

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
        pan = db.getPanel(panelID)
        par = pan['prevID']
        all_children = pan['nextIDs']
        child = [db.getPanel(ch_id) for ch_id in child_ids]
        comicID = ''
        comList = ''
        newComicButton = ('<a class="choice" href=\"' +
                         '/edit?prevID=' + panelID + 
                         '&comID' + comicID + '\">')
        for ch in child:
            comList = comList + comBut(ch['situation'], ch['startingPanelID'])
        if len(child) == 0:
            questionText = 'The End'
            newComicButton += 'Continue?'
        else:
            questionText = 'What happens next?'
            newComicButton += 'Or something else...'
        newComicButton += '</a>'
        return template('choose_template', panel=panelID, parent=par,
                        comicList=comList, questText=questionText,
                        newComicText=newComicText)

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

#run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

run(host='localhost', port=8000)
