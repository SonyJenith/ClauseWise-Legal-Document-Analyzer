def extract_text_from_image(image_bytes):
import easyocr
import numpy as np
import cv2

def extract_text_from_image(image_bytes):
    """Extract text from image bytes using EasyOCR (no Tesseract required)."""
    # Convert bytes to numpy array and then to image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    reader = easyocr.Reader(['en', 'hi', 'ta'], gpu=False)
    result = reader.readtext(img, detail=0)
    return '\n'.join(result)
