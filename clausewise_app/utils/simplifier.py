from .granite_model import get_granite_llm_translation

def simplify_clause(text):
    """Simplify a legal clause using the Granite LLM."""
    tokenizer, model = get_granite_llm_translation()
    prompt = f"Simplify this legal clause in plain English: {text}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=256)
    simplified = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return simplified
