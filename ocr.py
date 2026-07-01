import cv2
import pytesseract
from PIL import Image

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(path):

    # Read image
    img = cv2.imread(path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Apply thresholding
    _, thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Save temporary processed image
    temp_path = "temp_ocr.png"
    cv2.imwrite(temp_path, thresh)

    # OCR Text Extraction
    text = pytesseract.image_to_string(
        Image.open(temp_path),
        lang='san'
    )

    # OCR Confidence Score
    data = pytesseract.image_to_data(
        Image.open(temp_path),
        lang='san',
        output_type=pytesseract.Output.DICT
    )

    conf_values = []

    for conf in data["conf"]:
        try:
            conf = float(conf)

            if conf > 0:
                conf_values.append(conf)

        except:
            pass

    if len(conf_values) > 0:
        confidence = round(
            sum(conf_values) / len(conf_values),
            2
        )
    else:
        confidence = 0

    return text.strip(), confidence