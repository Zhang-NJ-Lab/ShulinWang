import pytesseract
from PIL import Image


def fun():
    pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract-OCR\tesseract.exe"
    image = Image.open(r"C:\Users\wang\Desktop\1.jpg", mode='r')
    #print(image)
    code = pytesseract.image_to_string(image)
    print(code)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    fun()

