# Multi-Engine OCR Web Application

A full-stack Python Flask application that allows users to upload images or PDFs and extract text using a variety of OCR engines, ranging from traditional Tesseract to modern Deep Learning models like EasyOCR and PaddleOCR.

## 🚀 Key Features
- **Unified Interface**: One frontend to access multiple OCR technologies.
- **Intelligent Routing**: Backend logic routes requests to the selected engine.
- **Preprocessing Pipeline**: Enhances image quality (grayscale, noise removal, thresholding) before sending to Tesseract.
- **PDF Support**: Automatically converts PDF pages to images for processing.
- **Deep Learning Integration**: Includes SOTA models (PaddleOCR, EasyOCR) running locally.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **OCR Engines**:
  - `pytesseract` (Tesseract OCR - Local, Rule-based)
  - `easyocr` (EasyOCR - Local, Deep Learning)
  - `paddleocr` (PaddleOCR - Local, Industrial Grade DL)
  - `google-cloud-vision` (Optional Cloud)
  - `boto3` (AWS Textract - Optional Cloud)
- **Image Processing**: OpenCV (`cv2`), Pillow, `pdf2image`

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- **Python 3.8+**
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)** installed and added to system PATH.
- **[Poppler](http://blog.alivate.com.au/poppler-windows/)** installed and added to system PATH (for PDF conversion).
- **Visual C++ Redistributable** (required for some Python libraries on Windows).

### 2. Quick Start (Windows)
We provide a PowerShell script to automate the setup (venv creation, dependency installation) and running of the app.
```powershell
.\setup_and_run.ps1
```

### 3. Manual Installation
1. Clone the repository and navigate to the folder:
   ```bash
   cd multi_ocr_app
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Cloud Credentials (Optional)
If you plan to use Google Vision or AWS Textract:
- **Google Cloud Vision**: Set `GOOGLE_APPLICATION_CREDENTIALS` env var.
- **AWS Textract**: Configure via AWS CLI or env vars.

### 5. Run Locally
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure
```
multi_ocr_app/
├── app.py                   # Main Flask Application
├── preprocessing/           # Image processing logic
│   └── image_preprocessing.py
├── ocr_engines/             # OCR Engine Wrappers
│   ├── tesseract_engine.py
│   ├── easyocr_engine.py    # [NEW] EasyOCR Wrapper
│   ├── paddle_engine.py     # [NEW] PaddleOCR Wrapper
│   ├── google_vision_engine.py
│   └── aws_textract_engine.py
├── templates/               # HTML
│   └── app.html             # Main Web Interface
├── static/                  # CSS, JS, Images
├── setup_and_run.ps1        # Automation Script
└── requirements.txt
```
