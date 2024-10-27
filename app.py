from flask import Flask, render_template, request
import pandas as pd
import requests
import base64
import spotipy

app = Flask(__name__)

# Replace with your own client id and client secret
CLIENT_ID = "89c0627f648b420ea35981271c55a2cc"
CLIENT_SECRET = "2507cde3e1c34b55828b2b16c2ba6434"

def get_access_token():
    # Base64 encode the client id and client secret
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_credentials_base64 = base64.b64encode(client_credentials.encode())

    # Request the access token
    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {client_credentials_base64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

def get_trending_playlist_data(playlist_id, access_token):
    # Set up spotipy with the access token
    sp = spotipy.Spotify(auth=access_token)

    # Get the tracks from the playlist
    playlist_tracks = sp.playlist_tracks(playlist_id, fields='items(track(id, name, artists, album(id, name)))')

    # Extract relevant information and store it in a list of dictionaries
    music_data = []
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
        track_id = track['id']

        # Get audio features for the track
        audio_features = sp.audio_features(track_id)[0] if track_id else None

        # Get release date of the album
        album_info = sp.album(album_id) if album_id else None
        release_date = album_info['release_date'] if album_info else None

        # Get popularity of the track
        track_info = sp.track(track_id) if track_id else None
        popularity = track_info['popularity'] if track_info else None

        # Add additional track information to the track data
        track_data = {
            'Track Name': track_name,
            'Artists': artists,
            'Album Name': album_name,
            'Album ID': album_id,
            'Track ID': track_id,
            'Popularity': popularity,
            'Release Date': release_date,
            'Duration (ms)': audio_features['duration_ms'] if audio_features else None,
            'Danceability': audio_features['danceability'] if audio_features else None,
            'Energy': audio_features['energy'] if audio_features else None,
            'Tempo': audio_features['tempo'] if audio_features else None,
            # Add more attributes as needed
        }

        music_data.append(track_data)

    # Create a pandas dataframe from the list of dictionaries
    df = pd.DataFrame(music_data)
    return df

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/playlist', methods=['POST'])
def playlist():
    playlist_id = request.form.get('playlist_id')
    access_token = get_access_token()

    if access_token:
        # Get the playlist data
        music_df = get_trending_playlist_data(playlist_id, access_token)
        # Convert the DataFrame to HTML to display in the template
        music_html = music_df.to_html(classes='table table-striped')
        return render_template('playlist.html', table=music_html)
    else:
        return "Error obtaining access token"

if __name__ == '__main__':
    app.run(debug=True)
