import pytesseract
import connexion
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'env\Tesseract-OCR\tesseract.exe'

# Create a handler for our read (POST)
def read_image():
    #reads sended image
    file = connexion.request.files['upfile']

    #converts formData to image
    image = Image.open(file)

    #reads text from image
    text = pytesseract.image_to_string(image, config='-l eng')

    return {'text': text}