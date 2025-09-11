#!/usr/bin/python3

"""Running a script with the waitress production server"""

from flask import Flask
from waitress import serve


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'> Alta3 simple server! </h1>"

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=2224)
