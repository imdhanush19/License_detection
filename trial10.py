import cv2
import pytesseract
import mysql.connector as ms

import serial
import time




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Specify the correct path

haarcascade = "haarcascade_russian_plate_number.xml"  # Provide the correct path or use the full path
license = cv2.CascadeClassifier(haarcascade)
def extract_plate(img_detect):
    img = cv2.imread(img_detect)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = license.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in nplate:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_img = img[y:y+h, x:x+w]
        modplate = license.detectMultiScale(roi_gray, 1.1, 4)
        read = pytesseract.image_to_string(roi_img)
        read=''.join(e for e in read if e.isalnum())
        print(read)
        cv2.imshow("DETECTED", img)
        return read
    

def database(detect):
    obj=ms.connect(host="",user='',passwd="",database="") #your own databae password and info
    if(obj.is_connected()):
        cur=obj.cursor()
        no=detect
        cur.execute("SELECT * FROM VEHICLE WHERE VEHICLE_NO='{}'".format(no))


        data=cur.fetchone()

        print(data[2])
        

detect=extract_plate("images.jpeg")
database(detect)
cv2.waitKey(0)
cv2.destroyAllWindows() 




