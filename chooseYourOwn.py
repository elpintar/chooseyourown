# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

from bottle import route, run, template

@route('/')
def home():
    return template('<b>Welocome</b>!')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)