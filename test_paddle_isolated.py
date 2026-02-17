import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

print("Testing PaddleOCR isolated...")
try:
    from ocr_engines.paddle_engine import ocr, extract_text
    print("PaddleOCR imported successfully.")
    
    # Create a dummy image or use an existing one if possible
    # For now just print that ocr object exists
    print(f"OCR Object: {ocr}")
    print("PaddleOCR test passed (initialization only).")
except Exception as e:
    print(f"PaddleOCR Failed: {e}")
    import traceback
    traceback.print_exc()
