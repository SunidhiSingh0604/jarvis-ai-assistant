import webbrowser
import pywhatkit
from voice.tts import say

def play_song_online(song_name):
    try:
        say(f"Playing {song_name} on YouTube")
        pywhatkit.playonyt(song_name)
    except:
        search_url = f"https://www.youtube.com/results?search_query={song_name}"
        webbrowser.open(search_url)
        say(f"Playing {song_name} on YouTube")
