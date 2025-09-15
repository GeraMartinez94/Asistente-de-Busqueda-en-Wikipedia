Descripción

Asistente de voz en español que permite al usuario dar comandos por voz para buscar información en Google y Wikipedia, y recibir respuestas habladas en tiempo real.

"busca en internet [término]" → devuelve la URL del primer resultado de Google.

"busca en wikipedia [término]" → lee un resumen de Wikipedia, oración por oración.

Requisitos

Python 3.12

Librerías:

pip install sounddevice soundfile speechrecognition pyttsx3 googlesearch-python wikipedia numpy

Estructura del proyecto
proyecto-ia/
├── main.py          # Archivo principal
├── voice_io.py      # Funciones de escucha y voz
└── search_engine.py # Funciones de búsqueda en Google y Wikipedia

Uso

Ejecuta el asistente:

python main.py


Di un comando por voz:

busca en internet inteligencia artificial


Devuelve la URL del primer resultado de Google.

busca en wikipedia inteligencia artificial


Lee un resumen de Wikipedia por oraciones.

Mejoras posibles

Añadir más comandos personalizados.

Mejorar la lectura de Wikipedia para evitar caracteres especiales.

Integrar APIs oficiales para resultados más precisos.
