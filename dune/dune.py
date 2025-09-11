#!/usr/bin/python3
"""To use, try:
    curl localhost:5000/
    curl localhost:5000/atreides/
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "In Frank Herbert's Dune, the Spice Melange makes space travel possible."


@app.route("/atreides")
def atreides():
    return "As Dune opens, House Atreides is transitioning their rule to Arrakis, a desert planet."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
