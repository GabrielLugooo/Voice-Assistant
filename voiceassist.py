
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
