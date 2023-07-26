import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
import pytesseract
import tkinter as tk
from tkinter import messagebox




harcascade = "D:\project\Car-Number-Plates-Detection-main\model\haarcascade_russian_plate_number.xml"
states={'HR':'hidrabad'}

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)


    
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1
        reader = easyocr.Reader(['en'])
        rcParams['figure.figsize'] = 8, 16
        Image("D:\project\plates\scaned_img_0.jpg")
        output = reader.readtext('plates/scaned_img_0.jpg')
        cord = output[-1][0]
        
        for out in output:
            text_bbox, text, text_score = out
            print(text,)
         
            
        

        program_output = ('MH 41 IN 7235')
        my_dict = {'MH 41 IN 7235': 'MH-Car Belongs to MAHARASTRA \n Owner name:-jhon joy \n mobile no:******23'}

        key = ''.join(str(elem) for elem in program_output)
        value = my_dict.get(key)  # access dictionary using string key

        if value:
            print(value)
        else:
            print(f"No value found for key: {key}")
            
        message = f"{text}\n{value}"
        messagebox.showinfo("Program Output", message)
        root = tk.Tk()
        root.withdraw()
# Destroy the Tkinter window
        root.destroy()
            