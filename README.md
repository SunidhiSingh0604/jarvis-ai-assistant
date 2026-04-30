# jarvis-ai-assistant
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis AI Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #222;
        }
        code, pre {
            background: #eee;
            padding: 10px;
            display: block;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        table, th, td {
            border: 1px solid #ccc;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        .section {
            margin-bottom: 40px;
        }
    </style>
</head>
<body>

<h1>🤖 Jarvis AI Assistant</h1>

<p>
A modular, voice-controlled AI assistant built in Python that automates daily tasks such as web browsing, music playback, real-time weather updates, and AI-powered conversations.
</p>

<p>
Designed with a clean architecture and separation of concerns, this project demonstrates practical skills in API integration, voice processing, and system design.
</p>

<hr>

<div class="section">
<h2>✨ Features</h2>
<ul>
<li><b>🎙️ Voice Recognition</b> – Captures and processes user commands using speech input.</li>
<li><b>🔊 Text-to-Speech (TTS)</b> – Converts responses into natural voice output.</li>
<li><b>🌐 Web Navigation</b> – Opens YouTube, Google, Instagram, Wikipedia.</li>
<li><b>🎵 Music Playback</b> – Plays songs directly on YouTube.</li>
<li><b>🌤️ Live Weather Updates</b> – Fetches real-time weather data.</li>
<li><b>🕐 Time Reporting</b> – Provides current system time.</li>
<li><b>🤖 AI Chat</b> – Conversational AI via Mistral 7B (OpenRouter).</li>
<li><b>💻 System Automation</b> – Opens Chrome, Notepad, Calculator, Camera.</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🧠 Architecture Overview</h2>

<pre>
jarvis-ai-assistant/
│
├── main.py
├── voice/
├── features/
├── config/
├── assets/
├── requirements.txt
├── README.md
</pre>

</div>

<hr>

<div class="section">
<h2>🛠️ Tech Stack</h2>

<table>
<tr><th>Technology</th><th>Purpose</th></tr>
<tr><td>Python</td><td>Core programming language</td></tr>
<tr><td>SpeechRecognition</td><td>Voice input processing</td></tr>
<tr><td>pyttsx3</td><td>Text-to-speech output</td></tr>
<tr><td>pywhatkit</td><td>YouTube automation</td></tr>
<tr><td>Requests</td><td>API communication</td></tr>
<tr><td>OpenWeatherMap API</td><td>Weather data</td></tr>
<tr><td>OpenRouter API (Mistral 7B)</td><td>AI conversation</td></tr>
</table>

</div>

<hr>

<div class="section">
<h2>🚀 Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
<li>Python 3.8+</li>
<li>Working microphone</li>
</ul>

<h3>Installation</h3>

<pre>
git clone https://github.com/YOUR_USERNAME/jarvis-ai-assistant.git
cd jarvis-ai-assistant
pip install -r requirements.txt
</pre>

<h3>Environment Setup</h3>

<pre>
OPENROUTER_API_KEY=your_api_key
WEATHER_API_KEY=your_api_key
</pre>

<h3>Run</h3>

<pre>
python main.py
</pre>

</div>

<hr>

<div class="section">
<h2>🗣️ Example Voice Commands</h2>

<table>
<tr><th>Command</th><th>Action</th></tr>
<tr><td>Open YouTube</td><td>Opens YouTube</td></tr>
<tr><td>What's the weather</td><td>Speaks weather</td></tr>
<tr><td>What's the time</td><td>Tells time</td></tr>
<tr><td>Play Believer on YouTube</td><td>Plays song</td></tr>
<tr><td>Jarvis, explain AI</td><td>Starts AI chat</td></tr>
<tr><td>Bye Jarvis</td><td>Stops assistant</td></tr>
</table>

</div>

<hr>

<div class="section">
<h2>⚠️ Security Note</h2>
<ul>
<li>.env file is ignored using .gitignore</li>
<li>API keys are not stored in the repository</li>
<li>Use config.example.py as a template</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🔮 Future Improvements</h2>
<ul>
<li>Add GUI (Tkinter / PyQt)</li>
<li>Wake word detection</li>
<li>Multi-turn conversation memory</li>
<li>Cross-platform support</li>
<li>Spotify / Calendar integration</li>
</ul>
</div>

<hr>

<div class="section">
<h2>📸 Demo</h2>
<p>Add screenshots or demo GIF in assets folder.</p>
</div>

<hr>

<div class="section">
<h2>👨‍💻 Author</h2>
<p><b>Your Name</b></p>
<p>
LinkedIn: https://linkedin.com/in/yourprofile<br>
Portfolio: https://yourportfolio.com
</p>
</div>

</body>
</html>
