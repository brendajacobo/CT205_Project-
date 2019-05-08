import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import credentials # external credentials module to hide sensitive OAuth information

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = 'Radiohead'

client_id = credentials.client_id # create 
client_secret = credentials.client_secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

result = sp.search(search_str)
pprint.pprint(result)