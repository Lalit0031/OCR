import cv2
import pytesseract
import pyttsx3

pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_img(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread(r'C:\Users\lalit\PycharmProjects\OCR\pic.jpeg')

print(ocr_img(img))
engine = pyttsx3.init()
engine.say(ocr_img(img))

engine.runAndWait()
engine.stop()