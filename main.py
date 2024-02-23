import pytesseract
from PIL import Image

# Replace the path below with the path to your image file
image_path = 'Screenshot 2024-02-22 at 21.36.21.png'

def extract_text(image_path):
    try:
        # Opening the image using PIL
        img = Image.open(image_path)

        # Extracting the text from the image
        text = pytesseract.image_to_string(img)

        return text
    except Exception as e:
        return f"An error occurred: {e}"

# Extracting text from the image
extracted_text = extract_text(image_path)

# Printing the extracted text
print(extracted_text)
