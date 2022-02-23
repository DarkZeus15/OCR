#pip install Pillow
from PIL import Image
#pip install pytesseract
from pytesseract import pytesseract as ptr

#Load the path of tesserract exe, Install tesseract.exe on your device and get the path from installed location
path_to_tesseract = r"C:\\Program Files (x86)\\Tesseract-OCR\tesseract.exe"

#Get image path, Read mode
image_path = r"C:\\Users\\Dark Zeus\\OneDrive\\Documents\\150 pages set (1021)\\150 pages set (1021)\\1.jpg"

#Open the image
img = Image.open(image_path)

#Provide executable location to tesseract library
ptr.tesseract_cmd=path_to_tesseract

#Save text from the image to some variable
text = ptr.image_to_string(img, lang='eng', config='--psm 8 -c page_separator=""')

#Print the collected text from the file
print("Collected text is :- \n",text)
