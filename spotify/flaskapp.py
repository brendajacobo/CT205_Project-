from flask import Flask
import spotify as sp
import smiledetector as sd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'