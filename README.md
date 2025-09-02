# ClauseWise

ClauseWise is an AI-powered legal document analyzer designed to simplify, decode, and classify complex legal texts for lawyers, businesses, and laypersons alike.

## Features
- **Clause Simplification**: Automatically rewrites complex legal clauses into simplified, layman-friendly language.
- **Named Entity Recognition (NER)**: Identifies and extracts key legal entities such as parties, dates, obligations, monetary values, and legal terms.
- **Clause Extraction and Breakdown**: Detects and segments individual clauses from lengthy legal documents.
- **Document Type Classification**: Classifies uploaded legal documents into categories like NDA, lease, employment contract, or service agreement.
- **Multi-Format Document Support**: Upload and process legal documents in PDF, DOCX, or TXT formats.
- **User-Friendly Interface**: Interactive frontend using Streamlit.


## Technologies & Tools
- Python
- Streamlit
- HuggingFace Transformers
- IBM Watson
- Granite (for generative AI, integrated)

## Getting Started

1. Install dependencies: `pip install -r requirements.txt`
2. (Optional, for Granite) Install the transformers library and ensure access to IBM Granite models:
	`pip install transformers`
	You may need to authenticate with HuggingFace or IBM for private models.
3. Run the app: `python -m streamlit run clausewise_app/app.py`


## Note
- Some features may require API keys or authentication for IBM Watson, HuggingFace, or Granite.
- Replace any placeholder keys in the code with your actual credentials.
- Granite model loading is available in `clausewise_app/utils/granite_model.py`.
