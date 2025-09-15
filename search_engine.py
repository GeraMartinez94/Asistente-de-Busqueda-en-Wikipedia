from googlesearch import search
import wikipedia

# Google: solo URL
def search_google(query):
    try:
        results = list(search(query, num_results=1))
        if results:
            return f"Encontré esto: {results[0]}"
        else:
            return "No encontré resultados en Google."
    except Exception as e:
        return f"No se pudo buscar en Google: {e}"

# Wikipedia: resumen de 2 frases
def search_wikipedia(query):
    try:
        wikipedia.set_lang("es")
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Tu búsqueda es ambigua. Algunas opciones: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No encontré nada en Wikipedia."
    except Exception as e:
        return f"Error al buscar en Wikipedia: {e}"
