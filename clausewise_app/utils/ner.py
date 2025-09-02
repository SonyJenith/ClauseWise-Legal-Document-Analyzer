from .granite_model import get_granite_llm_translation
import re

def extract_entities(text):
    """Extract legal entities using Granite LLM."""
    tokenizer, model = get_granite_llm_translation()
    prompt = (
        "Extract the following legal entities from this text as a JSON object: "
        "parties, dates, obligations, monetary values, legal terms.\nText: " + text
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(**inputs, max_length=256)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Try to extract JSON from result
    try:
        import json
        match = re.search(r'\{.*\}', result, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except Exception:
        pass
    return {"raw_output": result}
