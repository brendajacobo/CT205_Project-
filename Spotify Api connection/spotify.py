"""Spotify API connection"""

from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.spotify import make_spotify_blueprint, spotify
from flask_bootstrap import Bootstrap
import requests, json, urllib.parse
import spotipy
import json

blueprint = make_spotify_blueprint(
    client_id='16c88d48f61648acb6f1b11b28c1141b',
    client_secret='26b4701201704cf99ebe5f39184f14d4',
    scope='playlist-modify-public streaming user-library-read',
)

app = Flask(__name__)
app.secret_key = 'development'
Bootstrap(app)

app.register_blueprint(blueprint, url_prefix='/login')

@app.route('/')
def index():
    if not spotify.authorized:
        return redirect(url_for('spotify.login'))
    search_string = urllib.parse.quote('playlist/4nI5SVSGN1CHK8tLys1H39')
    resp = spotify.get(f'v1/search?q={search_string}&type=playlist')
    return render_template('home.html', data=resp.json())

