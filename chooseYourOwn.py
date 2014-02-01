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
	return '<a href=\"/read/' + panelID + '\">' + situation + '</a>'

@route("/")
def displayMenu():
	# The menu page, displays the list of comics
	comics = db.getAllComics()
	comList = ''
	for cm in comics:
		comList = strng + comBut(cm['situation'],
					 cm['startingPanelID'])
		comList = strgn + '\n'
	return template('menu_template', comicList = comList)

@route("/edit/<panel>")
def displayEdit(panel):
	# Returns the edit page
	return template('edit_template', panel=panel)

@post("/edit/<panel>")
def display_edit(panel):
	# Adds a new panel to the database and returns its ID.
	prevID = request.params['prevID']
	whatsHappening = request.params['whatsHappening']
	img = request.params['img']
	newID = db.newPanel(prevID, whatsHappening, img)
	return newID # TODO: does return work here? or do we have to do something with response?

@route("/read/<panel>")
def displayPanel(panel):
	# Returns the display screen for the given panel
	pan = db.getPanel(panel)
	img = pan['img']
	par = pan['prevID']
	children = pan['nextIDs']
	if len(children) == 0:
		nextLink = '/edit/' + panel
	elif len(pan['nextIDs']) < 3:
		nextLink = '/read/' + random.choice(pan['nextIDs'])
	else:
		nextLink = '/choose/' + panel
	return template('read_template', nextLink=nextLink, parent=par, img=img)

@route("/choose/<panel>")
def displayNext(panel):
	# Returns the next-panel decision screen
	pan = db.getPanel(panel)
	par = pan['prevID']
	all_children = pan['nextIDs']
	child_ids = random.sample(all_children, 3)
	child = [db.getPanel(ch_id) for ch_id in child_ids]
	desc = [ch['text'] for ch in child]
	return template('choose_template', panel=panel, parent=par,
			child0=child[0], child1=child[1], child2=child[2],
			desc0=desc[0], desc1=desc[1], desc2=desc2[2])
			

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
