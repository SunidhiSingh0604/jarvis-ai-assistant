![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![AI](https://img.shields.io/badge/AI-Mistral%207B-orange)
![API](https://img.shields.io/badge/API-OpenRouter-blueviolet)

# Jarvis AI Assistant

<p>
A modular, voice-controlled AI assistant built in Python that automates daily tasks such as web browsing, music playback, real-time weather updates, and AI-powered conversations.
</p>

<p>
Designed with a clean architecture and separation of concerns, this project demonstrates practical skills in API integration, voice processing, and system design.
</p>

<blockquote>
  💡 Built this because I wanted a hands-free way to manage my morning routine.
</blockquote>

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
├── 📄 <a href="./main.py">main.py</a>
├── 📁 <a href="./voice/">voice/</a>
│   ├── 📄 <a href="./voice/speech.py">speech.py</a>
│   └── 📄 <a href="./voice/tts.py">tts.py</a>
│
├── 📁 <a href="./features/">features/</a>
│   ├── 📄 <a href="./features/ai_chat.py">ai_chat.py</a>
│   ├── 📄 <a href="./features/music.py">music.py</a>
│   └── 📄 <a href="./features/weather.py">weather.py</a>
│
├── 📁 <a href="./config/">config/</a>
│   └── 📄 <a href="./config/settings.py">settings.py</a>
│
├── 📄 <a href="./config.example.py">config.example.py</a>
├── 📄 <a href="./requirements.txt">requirements.txt</a>
├── 📄 <a href="./README.md">README.md</a>
└── 📄 <a href="./.gitignore">.gitignore</a>
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
<p><b>Sunidhi Singh</b></p>
<p>📧 Connect with me on 
<a href="https://www.linkedin.com/in/sunidhi-singh-4aa45233b" target="_blank">
LinkedIn
</a>
</p>
</div>

