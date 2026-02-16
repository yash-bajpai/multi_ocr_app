from google.cloud import vision
import io
import os

def extract_text(image_path):
    """
    Extracts text from an image using Google Cloud Vision API.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Extracted text or error message.
    """
    if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
        return "Error: GOOGLE_APPLICATION_CREDENTIALS environment variable not set."

    try:
        client = vision.ImageAnnotatorClient()

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if response.error.message:
            return f"Error from Google Vision API: {response.error.message}"
        
        if texts:
            return texts[0].description.strip()
        else:
            return ""

    except Exception as e:
        return f"Error in Google Vision OCR: {str(e)}"
