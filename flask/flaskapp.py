from flask import Flask
import ../spotify/spotify as sp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'