import boto3
import os

def extract_text(image_path):
    """
    Extracts text from an image using AWS Textract.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Extracted text or error message.
    """
    # Quick check for credentials (though boto3 handles deeper checks)
    if not (os.environ.get("AWS_ACCESS_KEY_ID") and os.environ.get("AWS_SECRET_ACCESS_KEY")) and \
       not os.environ.get("AWS_PROFILE"):
         # This is a soft check; user might rely on ~/.aws/credentials
         pass 

    try:
        # Region verification is useful
        region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
        client = boto3.client('textract', region_name=region)

        with open(image_path, 'rb') as document:
            image_bytes = document.read()

        response = client.detect_document_text(Document={'Bytes': image_bytes})

        extracted_text = ""
        for item in response.get('Blocks', []):
            if item['BlockType'] == 'LINE':
                extracted_text += item['Text'] + "\n"
        
        return extracted_text.strip()

    except Exception as e:
        return f"Error in AWS Textract: {str(e)}"
