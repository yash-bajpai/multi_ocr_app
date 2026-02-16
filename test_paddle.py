import os
import sys

# Add project root to system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Disable network check for PaddleOCR
os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'

from ocr_engines import paddle_engine
from PIL import Image, ImageDraw, ImageFont

def create_test_image(text="Hello PaddleOCR", filename="test_paddle.png"):
    img = Image.new('RGB', (400, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    # Load default font
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
        
    d.text((50, 80), text, font=font, fill=(0, 0, 0))
    img.save(filename)
    return filename

def test_paddle():
    with open("test_output.txt", "w") as f:
        f.write("Testing PaddleOCR integration...\n")
        print("Testing PaddleOCR integration...")
        
        image_path = create_test_image()
        
        try:
            text = paddle_engine.extract_text(image_path)
            f.write(f"Extracted Text:\n{text}\n")
            print(f"Extracted Text:\n{text}")
            
            if "Hello PaddleOCR" in text:
                f.write("SUCCESS: PaddleOCR extracted the expected text.\n")
                print("SUCCESS: PaddleOCR extracted the expected text.")
            else:
                f.write("FAILURE: PaddleOCR did not extract the expected text.\n")
                print("FAILURE: PaddleOCR did not extract the expected text.")
                
        except Exception as e:
            f.write(f"ERROR: {str(e)}\n")
            print(f"ERROR: {str(e)}")
        finally:
            if os.path.exists(image_path):
                os.remove(image_path)

if __name__ == "__main__":
    test_paddle()
