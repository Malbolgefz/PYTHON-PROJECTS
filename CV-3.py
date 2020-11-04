from cv2 import cv2
import time


#import time

video=cv2.VideoCapture(0)

A=1
while True:  #SYNTAX OF INFINITE LOOP
   

    
   check,frame=video.read()

   print(check)
   print(frame)
   gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

   cv2.imshow("CAPTURED",gray)

   
   k = cv2.waitKey(20)   #waitkey function also give return the key which pressed during the waiting period in this case 20 millisecond.
   
                           
   if k == 27:
               # wait for ESC key to exit
        break
   A=A+1
   

print("NUMBER OF FRAMES SHOWN ON SCREEN=",A) #NUMBER OF FRAMES SHOWN ON SCREEN OR NUMBER OF TIMES WHILE LOOP ITERATED 



video.release()

cv2.destroyAllWindows()
