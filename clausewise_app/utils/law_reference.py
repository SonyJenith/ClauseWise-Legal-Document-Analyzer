# law_reference.py
"""
Utility to identify relevant acts of law and legal issues based on document content and selected country.
Stub implementation: Replace with ML/NLP or legal database integration for production.
"""

COUNTRY_LAWS = {
    "India": {
        "NDA": ["Indian Contract Act, 1872", "Information Technology Act, 2000"],
        "Lease Agreement": ["Transfer of Property Act, 1882"],
        "Employment Contract": ["Industrial Disputes Act, 1947", "Shops and Establishments Act"],
        "Service Agreement": ["Indian Contract Act, 1872"],
        # ...
    },
    "USA": {
        "NDA": ["Uniform Trade Secrets Act", "Defend Trade Secrets Act, 2016"],
        "Lease Agreement": ["State Landlord-Tenant Laws"],
        "Employment Contract": ["Fair Labor Standards Act", "State Employment Laws"],
        "Service Agreement": ["Uniform Commercial Code (UCC)"],
        # ...
    },
    # Add more countries and mappings as needed
}

EXPECTED_ISSUES = {
    "NDA": ["Breach of confidentiality", "Enforceability", "Jurisdiction"],
    "Lease Agreement": ["Eviction", "Security deposit disputes", "Maintenance obligations"],
    "Employment Contract": ["Wrongful termination", "Non-compete enforcement", "Wage disputes"],
    "Service Agreement": ["Non-performance", "Payment disputes", "Liability issues"],
    # ...
}

def get_law_references(doc_type, country):
    """Return relevant acts of law for the document type and country."""
    return COUNTRY_LAWS.get(country, {}).get(doc_type, ["No specific law found"])

def get_expected_legal_issues(doc_type):
    """Return common legal issues for the document type."""
    return EXPECTED_ISSUES.get(doc_type, ["No common issues found"])
