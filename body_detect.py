import cv2

img = cv2.imread("Walkers.py")

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

bodies = body_cascade.detectMultiScale(gray, 1, 2, 3)
print(body)

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
             
cv2.imshow('img',img)
cv2.waitKey(0)