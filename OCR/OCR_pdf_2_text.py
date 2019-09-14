"""

Using OCR(optical character recognition ) reading pdf data into text format
FOR LINUX SYSTEM PACKAGE INSTALLATION

#TO CONVERT PDF TO IMAGES
!sudo apt install poppler-utils
!pip install pdf2image

#TO CONVERT IMAGES TO TEXT FORMAT
!pip install pytesseract
!sudo apt install tesseract-ocr
"""

#CODE

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import sys

def pdf_2_image(file_name):
	try:
        pages = convert_from_path(file_name, 500)
        count=1
        for page in pages:
          str1='out'+str(count)+'.jpg'
          page.save(str1, 'JPEG')
          count=count+1
    except:
        print("unable to complete pdf_2_image")
        sys.exit()
        
        
def image_2_text(filename):
    try:
        return(text = pytesseract.image_to_string(Image.open(filename)))
    except:
        print("unable to convert image_2_text")
        sys.exit
        

if __init__== "__main__":
    pdf_2_image("temp.pdf")
    image_2_text("image.jpg")
    