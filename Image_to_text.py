import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def convert():
    img=Image.open('D:\Python\img.jpg')
    text=pt.image_to_string(img)
    print(text)
convert()