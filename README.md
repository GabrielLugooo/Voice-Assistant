<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# VOICE ASSISTANT

<a href="https://github.com/GabrielLugooo/Voice-Assistant" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Voice%20Assistant-000000" alt="English Voice Assistant" /></a>
<a href="https://github.com/GabrielLugooo/Voice-Assistant/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Voice%20Assistant-green" alt="Spanish Voice Assistant" /></a>

### Objective

This project aims to develop a simple voice assistant in Python that can recognize spoken commands and perform specific actions, such as searching for products on Amazon.

The assistant converts speech to text, interprets the command, and responds with synthetic voice, enhancing user interaction.

The goal is to learn how to integrate speech recognition and text-to-speech synthesis technologies into practical applications, providing an interactive and automated user experience.

### Skills Learned

- Implementation of voice recognition with SpeechRecognition.
- Use of text-to-speech synthesis with pyttsx3.
- Handling audio input and output.
- Opening web links based on voice commands.
- Using control flow structures in Python.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python
- SpeechRecognition
- pyttsx3
- Webbrowser

### Project

#### Code with Comments (English)

```python
# VoiceAssistant

# Install required dependencies
# Install pip install SpeechRecognition
# Install pip install pyttsx3
# The Amazon web search is https://www.amazon.es/s?k=

# Import required libraries
import speech_recognition as sr # For speech recognition
import webbrowser # For opening links in browser
import pyttsx3 # For converting text to speech

# Initialize speech recognizer
recognizer = sr. Recognizer()

# Initialize speech synthesis engine
engine = pyttsx3. init()

def talk():
"""
Captures audio input from microphone and converts it to text.
"""
mic = sr.Microphone()
with mic as source:
print("Listening...")
audio = recognizer.listen(source) # Listen to audio from microphone

text = recognizer.recognize_google(audio, language='en') # Convert audio to text
print(f'You said: {text}')
return text.lower()

# Check if the user mentions 'amazon' in the conversation
if 'amazon' in talk():
engine.say('What do you want to buy on Amazon') # Respond with voice
engine.runAndWait()
text = talk() # Listen to the product you want to search for
webbrowser.open(f'https://www.amazon.es/s?k={text}') # Open the search on Amazon
```

### Limitations

VoiceAssitant it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
