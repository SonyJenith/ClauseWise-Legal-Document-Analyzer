
import streamlit as st
import pandas as pd
from utils.file_loader import load_document
from utils.clause_extractor import extract_clauses
from utils.ner import extract_entities
from utils.simplifier import simplify_clause
from utils.classifier import classify_document
from utils.law_reference import get_law_references, get_expected_legal_issues
from utils.translation import get_translation_pipeline
from utils.ocr import extract_text_from_image
from utils.lang_detect import detect_language

st.set_page_config(page_title="ClauseWise - Legal Document Analyzer", layout="wide")
st.title("ClauseWise: AI-Powered Legal Document Analyzer")


st.sidebar.header("Upload Legal Document or Image")
uploaded_file = st.sidebar.file_uploader("Choose a legal document (PDF, DOCX, TXT, PNG, JPG)", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])


# Only ask for target language; source is auto-detected
st.sidebar.header("Translation Settings")
tgt_lang = st.sidebar.selectbox("Translate To", ["en", "hi", "ta"], index=0, format_func=lambda x: {"en": "English", "hi": "Hindi", "ta": "Tamil"}[x])
translate = get_translation_pipeline()


if uploaded_file:
    ext = uploaded_file.name.split('.')[-1].lower()
    if ext in ["png", "jpg", "jpeg"]:
        # OCR for image with language detection and manual override
        image_bytes = uploaded_file.read()
        # First, try OCR in English
        document_text = extract_text_from_image(image_bytes)
        # Detect language from OCR result
        detected_lang = detect_language(document_text)
        st.info(f"Detected OCR text language: {detected_lang}")
        # Allow user to override OCR language
        lang_map = {"en": "eng", "hi": "hin", "ta": "tam"}
        supported_langs = ["en", "hi", "ta"]
        ocr_lang = st.selectbox("OCR Language (auto-detected, override if needed)", options=supported_langs, index=supported_langs.index(detected_lang) if detected_lang in supported_langs else 0, format_func=lambda x: {"en": "English", "hi": "Hindi", "ta": "Tamil"}[x])
        if ocr_lang != "en" or detected_lang not in lang_map:
            st.warning("Make sure the correct Tesseract language data is installed for best OCR results.")
        # OCR with selected language
        import pytesseract
        from PIL import Image
        import io
        image = Image.open(io.BytesIO(image_bytes))
        try:
            document_text = pytesseract.image_to_string(image, lang=lang_map.get(ocr_lang, "eng"))
            st.info(f"Extracted text using OCR language: {ocr_lang}")
        except Exception as e:
            st.warning(f"Could not OCR with language {ocr_lang}: {e}")
        st.subheader("Extracted Text from Image")
        st.write(document_text)
    else:
        # Load and display document
        document_text = load_document(uploaded_file)
        st.subheader("Document Preview")
        st.write(document_text[:1000] + ("..." if len(document_text) > 1000 else ""))

    # Auto-detect source language
    detected_lang = detect_language(document_text)
    st.info(f"Detected document language: {detected_lang}")

    # Translation option
    if detected_lang != tgt_lang:
        if st.button(f"Translate document to {tgt_lang}"):
            # Check for empty text
            if not document_text or not document_text.strip():
                st.warning("No text found to translate. Please check your document or OCR settings.")
            else:
                # Check if language pair is supported
                supported_pairs = [("hi", "en"), ("ta", "en"), ("en", "hi"), ("en", "ta")]
                if (detected_lang, tgt_lang) not in supported_pairs:
                    st.warning(f"Translation from {detected_lang} to {tgt_lang} is not supported.")
                else:
                    try:
                        translated = translate(document_text, detected_lang, tgt_lang)
                        st.subheader(f"Translated Text ({tgt_lang})")
                        st.write(translated)
                        document_text = translated
                    except Exception as e:
                        st.error(f"Translation failed: {e}")

    # Clause Extraction
    st.subheader("Clause Extraction and Breakdown")
    clauses = extract_clauses(document_text)
    for i, clause in enumerate(clauses, 1):
        with st.expander(f"Clause {i}"):
            st.write(clause)
            # Clause Simplification
            if st.button(f"Simplify Clause {i}", key=f"simplify_{i}"):
                simple = simplify_clause(clause)
                st.info(simple)
            # NER
            if st.button(f"Extract Entities from Clause {i}", key=f"ner_{i}"):
                entities = extract_entities(clause)
                st.json(entities)

    # Document Type Classification
    st.subheader("Document Type Classification")
    doc_type = classify_document(document_text)
    st.success(f"Document Type: {doc_type}")

    # Law Reference Section
    st.subheader("Legal Reference & Issues")
    country = st.selectbox("Select Country for Law Reference", ["India", "USA"], index=0)
    acts = get_law_references(doc_type, country)
    st.write(f"**Relevant Acts of Law in {country}:**")
    for act in acts:
        st.markdown(f"- {act}")
    issues = get_expected_legal_issues(doc_type)
    st.write("**Expected Legal Issues:**")
    for issue in issues:
        st.markdown(f"- {issue}")
else:
    st.info("Please upload a legal document or image to begin analysis.")
