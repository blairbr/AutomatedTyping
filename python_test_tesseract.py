# A program to automate typing tests at https://www.speedtypingonline.com/typing-test
# version 1.0 made with student. in the future we plan to create methods and remove parts that are hard-coded

#step one: import packages
from PIL import Image
import pyautogui, sys, time, pytesseract, fileinput, cv2

#Step 2: set up the tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Step 3: Take a screenshot of the text you want, then save the image text to a string
img = pyautogui.screenshot(region=(128, 606, 800, 170))
img.save(r'C:\Users\bbrown2\Desktop\PythonMaterials\PythonScreenshots\typingText.jpg')
img = r'C:\Users\bbrown2\Desktop\PythonMaterials\PythonScreenshots\typingText.jpg'

print(pytesseract.image_to_string(Image.open(img)))

text = pytesseract.image_to_string(Image.open(img))

pyautogui.doubleClick(x=128, y=606, interval=0.25)

for letter in text:
    pyautogui.typewrite(letter)
    time.sleep(.0000000000000000000000001)

pyautogui.typewrite(' ')

#then make a method to repeat this over and over again 

print("Exiting program")