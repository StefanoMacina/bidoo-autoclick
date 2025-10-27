from PIL import Image
import pytesseract
import pyautogui
import cv2
import numpy as np
from time import sleep
import mouse

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
region = (1075, 285, 50, 50)

def getImg():
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screen.png')
    screenshot_np = np.array(screenshot)
    gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    return text.strip().replace('\n', '').replace(' ', '')

def compare(text, input):
    if(input == text):
        return True
    return False
    
while True:
    t = getImg()
    r = compare("0",t)
    if(r):
        sleep(0.3)
        mouse.click('left')
    print(t)
    print(r)
    #sleep(1/100)

