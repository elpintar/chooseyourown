# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
import random
from bottle import route, run, template

print MONGOHQ_URL

@route("/")
def hello_world():
	# The menue page, displays the list of comics
	return template("Hello World!")

@route("/edit/<panel>")
def display_edit(panel):
	# Returns the edit page
	return template('edit.html', panel=panel)

@route("/read/<panel>")
def display_panel(panel):
	# Returns the display screen for the given panel
	pan = db.getPanel(panel)
	img = pan['img']
	par = pan['prev_id']
	return template('read.html', panel=panel, parent=par, img=img)

@route("/choose/<panel>")
def display_next(panel):
	# Returns the next-panel decision screen
	pan = db.getPanel(panel)
	par = pan['prev_id']
	all_children = pan['next_ids']
	child_ids = random.sample(all_children, 3)
	child = [db.getPanel(ch_id) for ch_id in child_ids]
	desc = [ch['text'] for ch in child]
	return template('choose.html', panel=panel, parent=par,
			child0=child[0], child1=child[1], child2=child[2],
			desc0=desc[0], desc1=desc[1], desc2[2])
			

@get('/<filename:re:.*\.js>')
def javascripts(filename)
	return static_file(filename, root='static/js')

@get('<filename:re:.*\.css>')
def stylsheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# run(host='localhost', port=8080)
