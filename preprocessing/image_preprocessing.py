import cv2
import numpy as np
from PIL import Image

def preprocess_image(image_path):
    """
    Reads an image and applies preprocessing steps to improve OCR accuracy.
    Steps: Grayscale -> Noise Removal -> Thresholding.
    Returns the preprocessed image as a PIL Image object.
    """
    # Read image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Could not read image at {image_path}")

    # 1. Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Noise Removal (using Median Blur to remove salt-and-pepper noise)
    # Kernel size 3 is standard for document images
    denoised = cv2.medianBlur(gray, 3)

    # 3. Thresholding (Adaptive Thresholding for varying lighting conditions)
    # ADAPTIVE_THRESH_GAUSSIAN_C is often better than MEAN_C for text
    # blockSize 11, C 2 are tunable parameters
    threshold_img = cv2.adaptiveThreshold(
        denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Convert back to PIL Image for compatibility with pytesseract/other tools
    # OpenCV uses BGR/Gray, PIL uses RGB/L
    pil_img = Image.fromarray(threshold_img)
    return pil_img
