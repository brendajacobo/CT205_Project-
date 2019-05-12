from flask import Flask, render_template, request, redirect, url_for
from flask_dance.contrib.spotify import make_spotify_blueprint, spotify
from flask_bootstrap import Bootstrap
import requests, json, urllib.parse
import spotipy as sp
import requests, json
from pprint import pprint
#import smiledetector as sd


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
def homepage():
	if not spotify.authorized:
		return redirect(url_for('spotify.login'))
	html = render_template('home.html')
	return html

def index():
    if not spotify.authorized:
        return redirect(url_for('spotify.login'))
    search_string = urllib.parse.quote('spotify:user:7q6bntim8y6tivg1730gd26k6:playlist:3cO8zP0McOaWbvDsOARPyE')
    resp = spotify.get(search_string(f'v1/search?q={search_string}&type=playlist'))
    return render_template('home.html', data=resp.json())

if __name__ == '__main__':
	app.run(use_reloader=True, debug=True)

