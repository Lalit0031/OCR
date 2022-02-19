import cv2
import pytesseract
import pyttsx3

# you have to first download and install tesseract
pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe' #please add location according to you.

def ocr_img(img):
    text = pytesseract.image_to_string(img)  # this will extract text from image to string
    return text 

img = cv2.imread(r'C:\Users\lalit\PycharmProjects\OCR\pic.jpeg') # it reads the image

print(ocr_img(img))
engine = pyttsx3.init() # text to speech
engine.say(ocr_img(img))

engine.runAndWait()
engine.stop()
