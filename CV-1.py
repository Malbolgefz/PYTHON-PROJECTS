from cv2 import cv2
 


print(cv2.__version__)



image = cv2.imread("D:\\3-PROGRAMMING-LANG\\test_1.mp4", 1)  #DOUBLE SLASH IS COMPULSORY IN PATH 
print(image)
cv2.imshow("Over the Clouds", image)

cv2.waitKey(0)
cv2.destroyAllWindows()



