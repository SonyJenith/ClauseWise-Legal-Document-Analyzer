from .granite_model import get_granite_llm_translation

def classify_document(text):
    """Classify legal document type using Granite LLM."""
    tokenizer, model = get_granite_llm_translation()
    prompt = (
        "Classify the following legal document into one of these types: NDA, Lease Agreement, Employment Contract, Service Agreement, Purchase Agreement, Partnership Agreement, Power of Attorney, or Other.\nText: " + text
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=32)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result.strip()
