import cv2


face_cascade=cv2.CascadeClassifier("F:\\PYTHON\ALL-PROGRAMS\\opencv-master-REQUIRED-DATA\\data\\haarcascades_cuda\\haarcascade_frontalface_default.xml") #CREATING OBJECT OF CLASS cascadeClassifer



img1=cv2.imread("22.jpg")
gray_img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  ###cvtcolor is an function##



faces=face_cascade.detectMultiScale(gray_img,scaleFactor=2.05,minNeighbors=5) #IT RETURNS THE CORDINATES OF FACE

for x,y,w,h in faces:  #CORFINATES RETURNED BY faces IS STORED HERE IN VARIABLES x,y,w,h
    img1=cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("DDD",img1)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img1)
    cv2.destroyAllWindows()

#TODO:


#FIXME: