from transformers import pipeline

def get_translation_pipeline(target_lang="en"):
    """Return a HuggingFace translation pipeline for the target language. Splits long text to avoid token limit errors."""
    from transformers import pipeline
    import re
    model_map = {
        ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",
        ("ta", "en"): "Helsinki-NLP/opus-mt-ta-en",
        ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
        ("en", "ta"): "Helsinki-NLP/opus-mt-en-ta",
        # Add more as needed
    }
    def get_model(src, tgt):
        return model_map.get((src, tgt), None)
    def split_text(text, max_chars=400):
        # Split by sentences, paragraphs, or lines to keep chunks small
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunks = []
        current = ""
        for s in sentences:
            if len(current) + len(s) < max_chars:
                current += (" " if current else "") + s
            else:
                if current:
                    chunks.append(current)
                current = s
        if current:
            chunks.append(current)
        return chunks
    def translate(text, src_lang, tgt_lang):
        model_name = get_model(src_lang, tgt_lang)
        if not model_name:
            raise ValueError(f"No translation model for {src_lang}->{tgt_lang}")
        # Set a higher max_length for output tokens
        translator = pipeline("translation", model=model_name, max_length=10000)
        # Split text if too long
        chunks = split_text(text)
        results = []
        for chunk in chunks:
            if chunk.strip():
                out = translator(chunk, max_length=10000)[0]["translation_text"]
                results.append(out)
        return " ".join(results)
    return translate
