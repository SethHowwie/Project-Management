from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def coin_toss( ):
    return['Heads', 'Tails'][random.randint(0,1)]

