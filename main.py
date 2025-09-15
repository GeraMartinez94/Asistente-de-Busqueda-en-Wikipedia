import voice_io
import search_engine

def process_command(command):
    if "busca en internet" in command:
        query = command.replace("busca en internet", "").strip()
        voice_io.speak(f"Buscando en internet {query}.")
        response = search_engine.search_google(query)
        voice_io.speak(response)

    elif "busca en wikipedia" in command:
        query = command.replace("busca en wikipedia", "").strip()
        voice_io.speak(f"Buscando en Wikipedia {query}.")

        response = search_engine.search_wikipedia(query)

        # Revisar si hay resultados
        if not response or "No encontré" in response or "Error" in response:
            voice_io.speak(response)
        else:
            # Leer por oraciones para mayor naturalidad
            sentences = response.split('. ')
            for sentence in sentences:
                if sentence.strip():
                    voice_io.speak(sentence.strip())

    else:
        voice_io.speak("No entendí el comando. Intenta decir 'busca en internet' o 'busca en wikipedia'.")

def main():
    voice_io.speak("Hola, estoy listo para ayudarte. Dime un comando.")
    while True:
        command = voice_io.listen()
        if command:
            process_command(command.lower())

if __name__ == "__main__":
    main()
