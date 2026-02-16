
import easyocr

# Initialize reader once at module level to avoid reloading
# gpu=False is safer for broader compatibility unless CUDA is confirmed
reader = easyocr.Reader(['en']) 

def extract_text(image_path):
    """
    Extracts text from an image using EasyOCR.
    """
    try:
        # Read text
        result = reader.readtext(image_path, detail=0)
        
        # Join the list of strings into a single string
        return "\n".join(result)
    except Exception as e:
        return f"Error in EasyOCR: {str(e)}"
