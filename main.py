import os
import datetime
import webbrowser

from voice.speech import take_command
from voice.tts import say

from features.weather import get_weather
from features.music import play_song_online
from features.ai_chat import chat_with_ai

def main():
    say("Hello, I am Jarvis AI")

    while True:
        print("Listening...")
        query = take_command()

        if not query:
            continue

        if "bye jarvis" in query:
            say("Goodbye!")
            break

        handled = False

        # Websites
        sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "instagram": "https://www.instagram.com",
            "wikipedia": "https://www.wikipedia.com"
        }

        for site in sites:
            if f"open {site}" in query:
                say(f"Opening {site}")
                webbrowser.open(sites[site])
                handled = True

        # Time
        if "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The current time is {current_time}")
            handled = True

        # Weather
        if "weather" in query or "temperature" in query:
            say("Fetching weather")
            get_weather()
            handled = True

        # Music
        if "play" in query:
            song = query.replace("play", "").replace("on youtube", "").strip()
            if song:
                play_song_online(song)
            else:
                say("Tell me the song name")
            handled = True

        # Apps
        apps = {
            "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
            "notepad": "notepad",
            "calculator": "calc"
        }

        for app in apps:
            if f"open {app}" in query:
                if apps[app] in ["notepad", "calc"]:
                    os.system(apps[app])
                else:
                    os.startfile(apps[app])
                handled = True

        # Camera
        if "open camera" in query:
            say("Opening camera")
            os.system("start microsoft.windows.camera:")
            handled = True

        # AI Chat
        if not handled and "jarvis" in query:
            msg = query.replace("jarvis", "").strip()
            if msg:
                chat_with_ai(msg)
            else:
                say("Yes?")

if __name__ == "__main__":
    main()
