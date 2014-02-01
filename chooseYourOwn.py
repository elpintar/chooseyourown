# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
import random
from urllib import quote
from DataBase import DataBase
from bottle import route, run, template, post, get, static_file, request, response

db = DataBase()

def comBut(situation, panelID, comicName):
	# Return the button containing described with text, situation,
	# and links to /read/panelID
	return ('<a class="choice" href=\"' + comicName + '/read/?panelID=' +
		panelID + '\">' + situation + '</a>' + '\n')

@route("/")
def displayMenu():
	# The menu page, displays the list of comics
	comics = db.getAllComics()
	comList = ''
	for cm in comics:
		comicName = quote(cm['situation'].replace(' ', '-'))
		comList = strng + comBut(cm['situation'], cm['situation'],
					 cm['startingPanelID'])
	return template('menu_template', comicList = comList)

@post("/")
def createComic():
	situation = request.params['situation']
	return db.newComic(situation)

@delete("/")
def deleteComic():
	comID = request.params['comID']
	return db.deleteComic(comID)

@route("/<comic>/edit")
def displayEdit(comic):
	# Returns the edit page
	panel = request.query.panelID
	return template('edit_template', panel=panel)

@post("/<comic>/edit")
def display_edit(comic):
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
	return newID

@route("/<comic>/read")
def displayPanel(comic):
	# Returns the display screen for the given panel
	panel = request.query.panelID
	pan = db.getPanel(panel)
	img = pan['img']
	par = pan['prevID']
	children = pan['nextIDs']
	if len(children) == 0:
		nextLink = '/' + comic + '/edit?prevID=' + panel
	elif len(children) == 1:
		nextLink = '/' + comic + '/read?panelID=' + children[0]
	else:
		nextLink = '/' + comic + '/choose?prevID=' + panel
	return template('read_template', nextLink=nextLink, parent=par, img=img)

@route("/<comic>/choose")
def displayNext(comic):
	# Returns the next-panel decision screen
	panel = request.query.panelID
	pan = db.getPanel(panel)
	par = pan['prevID']
	all_children = pan['nextIDs']
	child = [db.getPanel(ch_id) for ch_id in child_ids]
	comicID = ''
	comList = ''
	newComicButton = ('<a class="choice" href=\"' + comicName +
			  '/edit?prevID=' + panelID + 
			  '&comicID' + comicID + '\">')
	for ch in child:
		comList = strng + comBut(ch['situation'],
					 ch['startingPanelID'])
		comList = strgn + '\n'
	if len(child) == 0:
		questionText = 'The End'
		newComicButton += 'Continue?'
	else:
		questionText = 'What happens next?'
		newComicButton += 'Or something else...'
	newComicButton += '</a>'
	
	return template('choose_template', panel=panel, parent=par,
			comicList=comList, questText=questionText,
			newComicText=newComicText)
			

# What follows is copied from the Internet.
# Thank you Internet.
@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('<filename:re:.*\.css>')
def stylsheets(filename):
	return static_file(filename, root='static/css')

@get('<filename:re:.*\.html>')
def stylsheets(filename):
	return static_file(filename, root='static/html')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

#run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

run(host='localhost', port=8000)
