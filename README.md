
# Data-Extractor-From-Spotify 🎶

This Flask application fetches data from Spotify playlists, including details about tracks, artists, albums, and audio features like danceability and tempo. It displays this data in a simple web interface, making it easy to explore Spotify's trending playlists!

## Features
- Fetches data from any Spotify playlist by entering the playlist ID.
- Displays track information including:
  - Track Name
  - Artist(s)
  - Album Name and Release Date
  - Popularity, Danceability, Energy, Tempo, and Duration
- Presents data in an HTML table.

## Prerequisites

To run this project, you'll need:
- **Python 3.7+**
- **Spotify Developer Account** - to obtain your `CLIENT_ID` and `CLIENT_SECRET`.

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Vishal2053/Data-Extractor-From-Spotify.git
cd Data-Extractor-From-Spotify


### 2. Install Requirements
Use pip to install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up Your Spotify API Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new app to get your `CLIENT_ID` and `CLIENT_SECRET`.
3. Replace the `CLIENT_ID` and `CLIENT_SECRET` in `app.py` with your credentials.

### 4. Run the App
Run the Flask app:
```bash
python app.py
```

The app will run locally on `http://127.0.0.1:5000`.

### 5. Access the App
1. Open a web browser.
2. Go to `http://127.0.0.1:5000`.
3. Enter a Spotify playlist ID and view the playlist data.

## File Structure

- **app.py**: The main Flask application with routes and helper functions.
- **templates/index.html**: The homepage form to enter the playlist ID.
- **templates/playlist.html**: The page that displays playlist data in an HTML table.
- **requirements.txt**: Lists all dependencies.

## Spotify API Usage

The application authenticates with Spotify using the `client_credentials` flow and retrieves data about playlist tracks, including their audio features and popularity. The `spotipy` library is used to handle Spotify API requests.

## Important Files

- **app.py** - main application file
- **templates/index.html** - input form for playlist ID
- **templates/playlist.html** - displays playlist data in table format

## Sample Playlist ID

You can use the playlist ID from any Spotify playlist URL:
- **Example URL**: `https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M`
- **Playlist ID**: `37i9dQZF1DXcBWIGoYBM5M`

## Technologies Used

- **Flask** - Web framework for handling requests and rendering templates.
- **Spotipy** - Python client for the Spotify Web API.
- **Pandas** - For data handling and DataFrame creation.
- **HTML/CSS** - For rendering data in a structured and styled format.

## Troubleshooting

- **Access Token Error**: If you encounter an "Error obtaining access token," double-check your `CLIENT_ID` and `CLIENT_SECRET`.
- **API Rate Limits**: Spotify has rate limits on API requests. Avoid making too many requests in a short time.
- **Playlist ID**: Make sure the playlist ID is valid.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API integration in Python.
- [Spotify Developer API](https://developer.spotify.com/) for enabling access to rich music data.

---

**Note**: This project is for educational purposes and does not represent a production-level application. Always keep API keys and sensitive information secure.
```

Make sure to replace `https://github.com/yourusername/flask-spotify-playlist-tracker.git` with the correct URL for your repository.