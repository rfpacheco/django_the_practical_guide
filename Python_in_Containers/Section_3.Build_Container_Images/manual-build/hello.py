# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello, World! Greetings from a Container!"
