# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
from bottle import route, run

@route("/")
def hello_world():
    return "Hello World!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# run(host='localhost', port=8080)