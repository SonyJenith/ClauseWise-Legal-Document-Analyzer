def load_document(uploaded_file):
    """Load and extract text from PDF, DOCX, TXT, or image file (PNG, JPG, JPEG)."""
    import pdfplumber
    from docx import Document
    import io
    ext = uploaded_file.name.split('.')[-1].lower()
    if ext == 'pdf':
        with pdfplumber.open(uploaded_file) as pdf:
            return '\n'.join(page.extract_text() or '' for page in pdf.pages)
    elif ext == 'docx':
        doc = Document(uploaded_file)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif ext == 'txt':
        return uploaded_file.read().decode('utf-8')
    elif ext in ['png', 'jpg', 'jpeg']:
        from .ocr import extract_text_from_image
        image_bytes = uploaded_file.read()
        return extract_text_from_image(image_bytes)
    else:
        return "Unsupported file format."
