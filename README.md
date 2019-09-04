# Text Recognition API

Python Project - Text Recognition API with Connexion, Swagger and Tesseract OCR

## Author

#### Italo Nabuco<br>Full Stack Developer<br>
italonabuco@hotmail.com<br>

## Install Requirements

* connexion
* pytesseract
* tesseract-ocr
* PIL

## Usage

1. Set your tesseract_cmd at `file.py`if you've installed Tesseract through a .exe file.<br>
i.e.
```python
[...]
import pytesseract
import connexion
from PIL import Image

# change file path according to your installation folder.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
[...]
```

2. Executing project
    
    1. Open the terminal at your project's folder.
    2. type ```python server.py```

## Image Samples

### Image used for testing
<img src="https://github.com/italonabuco/text-recognition-api/blob/master/sample/phrase.jpeg" width="200">

### API call using PostMan
<img src="https://github.com/italonabuco/text-recognition-api/blob/master/sample/sample-result.PNG" width="900">
