import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import tempfile
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen(duration=5):
    """
    Escucha la voz del usuario durante 'duration' segundos y devuelve el texto reconocido.
    """
    fs = 44100  # frecuencia de muestreo
    print("🎙️ Escuchando...")

    # grabar audio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # crear archivo temporal seguro
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        temp_filename = temp_wav.name
    # escribir audio después de cerrar el archivo
    sf.write(temp_filename, recording, fs)

    # reconocer voz
    with sr.AudioFile(temp_filename) as source:
        audio = recognizer.record(source)

    # borrar archivo temporal
    try:
        os.unlink(temp_filename)
    except PermissionError:
        print("⚠️ No se pudo borrar el archivo temporal, pero no afecta la ejecución.")

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"👤 Tú dijiste: {text}")
        return text
    except sr.UnknownValueError:
        print("🤔 No entendí el audio.")
        return None
    except sr.RequestError:
        print("⚠️ Error con el servicio de reconocimiento de voz.")
        return None

def speak(text):
    """
    Convierte texto a voz y lo reproduce.
    """
    print(f"🤖 IA: {text}")
    engine.say(text)
    engine.runAndWait()
