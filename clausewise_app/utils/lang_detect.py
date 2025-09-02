from langdetect import detect

def detect_language(text):
    """Detect the language of the given text using langdetect."""
    try:
        lang = detect(text)
        return lang
    except Exception:
        return "unknown"
