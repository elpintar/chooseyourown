# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
import random
from DataBase import DataBase
from bottle import route, run, template, post, get, static_file, request, response

db = DataBase()

def comBut(situation, panelID):
	# Return the button containing described with text, situation,
	# and links to /read/panelID
	return ('<a class="choice" href=\"/read/' + panelID + '\">' + 
		situation + '</a>' + '\n')

@route("/")
def displayMenu():
	# The menu page, displays the list of comics
	comics = db.getAllComics()
	comList = ''
	for cm in comics:
		comList = strng + comBut(cm['situation'],
					 cm['startingPanelID'])
	return template('menu_template', comicList = comList)

@route("/edit/<comic>/<panel>")
def displayEdit(panel):
	# Returns the edit page
	return template('edit_template', panel=panel)

@post("/edit/<comic>/<panel>")
def display_edit(panel):
	# Adds a new panel to the database and returns its ID.
	prevID = request.params['prevID']
	whatsHappening = request.params['whatsHappening']
	img = request.params['img']
	newID = db.newPanel(prevID, whatsHappening, img)
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
		nextLink = '/' + comic + '/edit/' + panel
	elif len(children) == 1:
		nextLink = '/' + comic + '/read/' + children[0]
	else:
		nextLink = '/' + comic + '/choose/' + panel
	return template('read_template', nextLink=nextLink, parent=par, img=img)

@route("/choose/<comic>/<panel>")
def displayNext(panel):
	# Returns the next-panel decision screen
	panel = request.query.panelID
	pan = db.getPanel(panel)
	par = pan['prevID']
	all_children = pan['nextIDs']
	child = [db.getPanel(ch_id) for ch_id in child_ids]
	comList = ''
	for ch in child:
		comList = strng + comBut(ch['situation'],
					 ch['startingPanelID'])
		comList = strgn + '\n'
	if len(child) == 0:
		questionText = 'The End'
		newComicText = 'Continue?'
	else:
		questionText = 'What happens next?'
		newComicText = 'Or something else...'
	
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
