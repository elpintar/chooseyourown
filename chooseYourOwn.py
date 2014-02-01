# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
from bottle import route, run, template

print MONGOHQ_URL

@route("/")
def hello_world():
    return template("Hello World!"

@route("/edit/<panel>")
def display_edit(panel):
	# Returns the edit page
	return "Edit Page For " + panel

@route("/display/<panel>")
def display_panel(panel):
	# Returns the display screen for the given panel
	return "Display Page For " + panel

@route("/next/<panel>")
def display_next(panel):
	# Returns the next-screen for the given panel
	return "Next Page For " + panel

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# run(host='localhost', port=8080)
