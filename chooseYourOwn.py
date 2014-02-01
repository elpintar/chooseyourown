# Erik Pintar, Connor Brem, Spencer Barton, Billy Wood
# TartanHacks  2014

import os
from bottle import route, run

print MONGOHQ_URL

@route("/")
def hello_world():
    return template("Hello World!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# run(host='localhost', port=8080)