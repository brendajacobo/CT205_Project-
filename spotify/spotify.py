# import pprint
# import sys

# import spotipy
# import spotipy.util as util

# client_id = 'cf8915522beb40e0892bb9a05ebe9459' # Your client id
# client_secret = '05ca767fb8824188b731d68999ceadec' # Your secret
# redirect_uri = 'http://localhost:5000/' # Your redirect uri


# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()

# scope = 'playlist-modify-public'
# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
#     print(results)
# else:
#     print("Can't get token for" + username)


import spotipy
sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])