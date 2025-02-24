<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# GENERADOR DE CONTRASEÑAS

<a href="https://github.com/GabrielLugooo/Voice-Assistant/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Asistente%20Voz%20Español-000000" alt="Asistente Español" /></a>
<a href="https://github.com/GabrielLugooo/Voice-Assistant" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Asistente%20Voz%20Inglés-green" alt="Asistente Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo desarrollar un asistente de voz simple en Python que pueda reconocer comandos hablados y realizar acciones específicas, como realizar búsquedas en Amazon.

El asistente convierte la voz en texto, interpreta el comando y responde con voz sintética, mejorando así la interacción con el usuario.

El propósito es aprender a integrar tecnologías de reconocimiento de voz y síntesis de texto a voz en aplicaciones prácticas, proporcionando una experiencia de usuario interactiva y automatizada.

### Habilidades Aprendidas

- Implementación de reconocimiento de voz con SpeechRecognition.
- Uso de síntesis de voz con pyttsx3.
- Manipulación de entrada y salida de audio.
- pertura de enlaces web basados en comandos de voz.
- Uso de estructuras de control de flujo en Python.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python
- SpeechRecognition
- pyttsx3
- Webbrowser

### Proyecto

#### Código con Comentarios (Español)

```python
# VoiceAssistant

# Instalar dependencias necesarias:
# pip install SpeechRecognition
# pip install pyttsx3
# La web de búsqueda de Amazon es https://www.amazon.es/s?k=

# Importar las librerías necesarias
import speech_recognition as sr  # Para reconocimiento de voz
import webbrowser  # Para abrir enlaces en el navegador
import pyttsx3  # Para convertir texto a voz

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

def talk():
    """
    Captura la entrada de audio del micrófono y la convierte en texto.
    """
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        audio = recognizer.listen(source)  # Escucha el audio del micrófono

    text = recognizer.recognize_google(audio, language='es')  # Convierte el audio en texto
    print(f'Dijiste: {text}')
    return text.lower()

# Comprobar si el usuario menciona 'amazon' en la conversación
if 'amazon' in talk():
    engine.say('Que quieres comprar en Amazon')  # Responde con voz
    engine.runAndWait()
    text = talk()  # Escuchar el producto que desea buscar
    webbrowser.open(f'https://www.amazon.es/s?k={text}')  # Abre la búsqueda en Amazon

```

### Limitaciones

El Asistente de Voz es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
