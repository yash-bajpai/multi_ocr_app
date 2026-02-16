# Multi-Engine OCR Web Application

A full-stack Python Flask application that allows users to upload images or PDFs and extract text using one of three OCR engines: **Tesseract (Local)**, **Google Cloud Vision**, or **AWS Textract**.

## 🚀 Key Features
- **Unified Interface**: One frontend to access multiple OCR technologies.
- **Intelligent Routing**: Backend logic routes requests to the selected engine.
- **Preprocessing Pipeline**: Enhances image quality (grayscale, noise removal, thresholding) before sending to Tesseract.
- **PDF Support**: Automatically converts PDF pages to images for processing.

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **OCR Engines**:
  - `pytesseract` (Tesseract OCR)
  - `google-cloud-vision`
  - `boto3` (AWS Textract)
- **Image Processing**: OpenCV (`cv2`), Pillow, `pdf2image`

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to system PATH.
- [Poppler](http://blog.alivate.com.au/poppler-windows/) installed and added to system PATH (for PDF conversion).

### 2. Installation
1. Clone the repository and navigate to the folder:
   ```bash
   cd multi_ocr_app
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Cloud Credentials Configuration
- **Google Cloud Vision**:
  - Set the environment variable:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
    # Windows (PowerShell):
    # $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\service-account.json"
    ```
- **AWS Textract**:
  - Configure via AWS CLI (`aws configure`) or set env vars (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`).

### 4. Run Locally
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 🧠 Interview Explanation Guide

### 1. Project Architecture
The application follows a **Controller-Service** pattern. `app.py` acts as the controller, handling HTTP requests and file uploads. It utilizes a **Factory Pattern** (`get_ocr_engine`) to instantiate the correct engine service based on user input.

### 2. Preprocessing vs. Cloud AI
- **Tesseract** is an "engine", meaning it strictly translates pixels to text using pattern recognition. It requires **clean input**. That's why I implemented a preprocessing pipeline using OpenCV (Grayscale -> Median Blur -> Adaptive Thresholding) to improve accuracy on noisy documents.
- **Cloud APIs (Google/AWS)** use **Deep Learning** models trained on massive datasets. They don't just "read" text; they understand context, layout, and can handle noisy, rotated, or handwritten text without manual preprocessing.

### 3. Why Multiple Engines? (Trade-offs)
| Feature | Tesseract | Google Vision / AWS Textract |
|---------|-----------|------------------------------|
| **Cost** | Free (Open Source) | Pay-per-use |
| **Privacy** | Data stays local | Data sent to cloud |
| **Accuracy** | Good for clean typewritten text | Excellent for handwriting/complex layouts |
| **Speed** | Fast (runs locally) | Latency (network calls) |

### 4. Challenges Solved
- **PDF Handling**: OCR engines typically process images. I used `pdf2image` to rasterize PDF pages into images, enabling a uniform processing pipeline for both formats.
- **Modularity**: New engines can be added by simply creating a new module in `ocr_engines/` with an `extract_text` function, adhering to the implicit interface (Duck Typing).

---

## 📂 Project Structure
```
multi_ocr_app/
├── app.py                   # Main Flask Application
├── preprocessing/           # Image processing logic
│   └── image_preprocessing.py
├── ocr_engines/             # OCR Engine Wrappers
│   ├── tesseract_engine.py
│   ├── google_vision_engine.py
│   └── aws_textract_engine.py
├── templates/               # HTML
│   └── index.html
├── static/                  # CSS
│   └── style.css
└── requirements.txt
```
