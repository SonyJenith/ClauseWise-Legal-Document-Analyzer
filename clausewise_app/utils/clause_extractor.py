def extract_clauses(text):
    """Naive clause extraction: split by double newlines or semicolons. Replace with ML model for production."""
    import re
    # Try to split by numbered clauses or semicolons
    clauses = re.split(r'\n\d+\.\s|;|\n\n', text)
    return [c.strip() for c in clauses if c.strip()]
